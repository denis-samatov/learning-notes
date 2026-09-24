# PySpark Learning

A collection of focused, single-topic Jupyter notebooks covering PySpark DataFrame
operations — each notebook is a short, runnable example of one specific transformation
or pattern, rather than one long tutorial.

## Structure

- `notebooks/` — one notebook per PySpark topic (see below).

## Topics covered

All 19 notebooks in `notebooks/`, grouped by theme:

- **DataFrame basics**: `pyspark_create_dataframe.ipynb`, `pyspark_create_dataframe_dictionary.ipynb`, `pandas_pyspark_dataframe.ipynb`, `pyspark_collect.ipynb`.
- **Column operations**: `pyspark_add_new_column.ipynb`, `pyspark_cast_column.ipynb`, `pyspark_change_string_double.ipynb`, `pyspark_column_functions.ipynb`, `pyspark_column_operations.ipynb`, `convert_column_python_list.ipynb`, `pyspark_array_string.ipynb`, `pyspark_arraytype.ipynb`.
- **Aggregation & counting**: `pyspark_aggregate.ipynb`, `pyspark_count_distinct.ipynb`, `pyspark_broadcast_dataframe.ipynb`.
- **Maps & structs**: `pyspark_convert_columns_to_map.ipynb`, `pyspark_convert_map_to_columns.ipynb`.
- **Date handling**: `current_date.ipynb`, `pyspark_add_month.ipynb`.

## Getting started

1. Clone the consolidated repository and enter this section:
    ```sh
    git clone https://github.com/denis-samatov/learning-notes.git
    cd learning-notes/pyspark
    ```
2. Ensure a Java runtime compatible with your PySpark release is available,
   then create a Python environment and install the notebook dependencies:
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    python -m pip install pyspark notebook pandas
    ```
   On Windows, use `.venv\Scripts\activate` instead of the `source` command.
3. Launch Jupyter and open a notebook in `notebooks/`:
    ```sh
    jupyter notebook notebooks/
    ```

Each notebook is self-contained — start with `pyspark_create_dataframe.ipynb` if
you're new to PySpark, then explore the rest in any order. The notebooks also
contain historical `!pip install pyspark` cells; those are redundant after the
environment setup above. Saved outputs are examples from earlier runs, and the
repository does not pin dependency versions or run these notebooks in CI.
