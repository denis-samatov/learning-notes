"""Opt-in tiny local Spark checks; no remote cluster or downloads."""
import json
import os
from pathlib import Path

import pytest

pytestmark = pytest.mark.skipif(os.environ.get("RUN_SPARK_TESTS") != "1", reason="Spark/JVM runtime opt-in required: RUN_SPARK_TESTS=1")

@pytest.fixture(scope="module")
def spark():
    from pyspark.sql import SparkSession
    session = (SparkSession.builder.master("local[1]").appName("recipe-tests")
               .config("spark.driver.host", "127.0.0.1")
               .config("spark.driver.bindAddress", "127.0.0.1")
               .config("spark.ui.enabled", "false")
               .config("spark.sql.session.timeZone", "UTC").getOrCreate())
    try:
        yield session
    finally:
        session.stop()

@pytest.mark.parametrize("name", ["pyspark_collect.ipynb", "pyspark_count_distinct.ipynb", "pyspark_convert_map_to_columns.ipynb"])
def test_original_recipe_assertions(spark, name):
    path = Path(__file__).parents[1] / "notebooks" / name
    ns = {"__name__": "__main__"}
    for cell in json.loads(path.read_text())["cells"]:
        if cell["cell_type"] != "code": continue
        source = "".join(cell["source"])
        if any(line.lstrip().startswith(("!", "%")) for line in source.splitlines()): continue
        exec(compile(source, name, "exec"), ns)

def test_null_empty_schema_and_utc_date_contract(spark):
    from pyspark.sql import functions as F
    schema = "id int, value string"
    frame = spark.createDataFrame([(1, "2"), (2, None)], schema)
    values = frame.orderBy("id").select(F.col("value").cast("int")).collect()
    assert [row[0] for row in values] == [2, None]
    assert spark.createDataFrame([], schema).count() == 0
    assert frame.schema.simpleString() == "struct<id:int,value:string>"
    row = spark.range(1).select(F.to_date(F.lit("2024-02-29")).alias("date")).first()
    assert str(row.date) == "2024-02-29"
