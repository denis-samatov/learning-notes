"""Run opt-in local Spark recipes in a disposable working directory."""
import os
from pathlib import Path
import subprocess
import sys
import tempfile

root = Path(__file__).resolve().parents[1]
env = {key: value for key, value in os.environ.items()
       if not key.startswith(("SPARK_", "PYSPARK_"))}
env.update(RUN_SPARK_TESTS="1", SPARK_LOCAL_IP="127.0.0.1",
           PYSPARK_PYTHON=sys.executable, PYSPARK_DRIVER_PYTHON=sys.executable,
           PYTHONDONTWRITEBYTECODE="1")
with tempfile.TemporaryDirectory(prefix="learning-spark-") as tmp:
    subprocess.run([sys.executable, "-m", "pytest", str(root / "pyspark/tests"), "-q"],
                   cwd=tmp, env=env, check=True)
