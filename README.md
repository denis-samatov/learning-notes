# PySpark Learning

A collection of focused, single-topic Jupyter notebooks covering PySpark DataFrame
operations — each notebook is a short, runnable example of one specific transformation
or pattern, rather than one long tutorial.

## Structure

- `notebooks/` — one notebook per PySpark topic (see below).

## Topics covered

- **DataFrame basics**: creating DataFrames from Python lists/dicts, converting
  pandas ↔ PySpark DataFrames.
- **Column operations**: adding/casting columns, string ↔ double conversion,
  array/string handling, `ArrayType` columns.
- **Aggregation & counting**: `count_distinct`, aggregate functions, broadcasting a
  DataFrame for join optimization.
- **Maps & structs**: converting columns to a map and back.
- **Date handling**: current date, adding months to a date column.

## Getting started

1. Clone the repository:
    ```sh
    git clone https://github.com/denis-samatov/pyspark_learning.git
    cd pyspark_learning
    ```
2. Install PySpark and Jupyter:
    ```sh
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    pip install pyspark jupyter pandas
    ```
3. Launch Jupyter and open any notebook in `notebooks/`:
    ```sh
    jupyter notebook
    ```

Each notebook is self-contained — start with `pyspark_create_dataframe.ipynb` if
you're new to PySpark, then explore the rest in any order.
