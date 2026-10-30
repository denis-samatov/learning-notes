# Learning Notes

Personal reference material and learning notebooks, consolidated from four
previously separate repositories (histories preserved via `git subtree` --
see each section's own commit history for its original timeline). None of
this is original engineering; it's kept for personal reference and as a
public record of learning-in-progress, not as showcase work.

## Sections

- [`algorithms/`](algorithms/) -- Jupyter notebooks on binary search, binary
  trees, dictionary/counting sort, linear search, prefix sums and two
  pointers, and sorting events. **Some notebook content is in Russian**
  (personal notes, not translated -- see [Language](#language) below).
- [`pyspark/`](pyspark/) -- 19 focused, single-topic notebooks on PySpark
  DataFrame operations (creation, column operations, aggregation, maps/structs,
  date handling).
- [`genetic-algorithms/`](genetic-algorithms/) -- Two notebooks on genetic
  algorithms using DEAP (Distributed Evolutionary Algorithms in Python).
- [`docker/`](docker/) -- A Docker command reference/cheat sheet (no code).

## Language

Most content here is in English. `algorithms/` contains some notebooks with
Russian-language comments and markdown from when it was originally written --
these are left as personal notes rather than translated, since they're not
meant to be a polished public artifact.

## Using the notebooks

Start with the README in the section you want to explore. The PySpark notes
have a [local setup guide](pyspark/README.md#getting-started); the genetic
algorithm notebooks require DEAP, NumPy, and Matplotlib. Saved notebook
outputs document earlier runs, not a fresh execution of the current
environment. `genetic-algorithms/requirements-tested.txt` records the partial
locally tested profile; it is not a complete cross-platform lock.

## Regression checks

The Python 3.13 CI workflow uses two independent hash-locked environments because the recorded GA and Spark profiles have different NumPy versions. For algorithms and GA:

```sh
python -m pip install --require-hashes -r .ci/requirements-ga.lock
python -m pip check
python -m pip_audit --no-deps --disable-pip --strict -r .ci/requirements-ga.lock
MPLBACKEND=Agg python -m pytest algorithms/tests genetic-algorithms/tests -q
```

In a separate environment, with Java 21 available:

```sh
python -m pip install --require-hashes -r .ci/requirements-spark.lock
python -m pip check
python -m pip_audit --no-deps --disable-pip --strict -r .ci/requirements-spark.lock
python .ci/run_spark_tests.py
```

The Spark launcher binds a tiny `local[1]` session to loopback, clears inherited Spark runtime settings, runs in a temporary directory and stops the session in the fixture. It executes the three repaired notebook recipes and null/empty/schema/date assertions; the static test parses all 19 Spark notebooks. The GA tests check seeded repeatability and known minima; algorithm tests compare edge cases against brute-force oracles. These synthetic checks do not establish large-data performance or qualify every notebook's runtime.

Regenerate GA hashes with `uv pip compile .ci/requirements-ga.in --python-version 3.13 --generate-hashes -o .ci/requirements-ga.lock`. `.ci/requirements-spark.in` records the complete pinned Python 3.13 Linux validation dependency closure; use `uv pip compile .ci/requirements-spark.in --no-deps --python-version 3.13 --generate-hashes -o .ci/requirements-spark.lock` to refresh hashes. Review and revalidate the closure when updating versions. Advisory checks cover these profiles, not every possible notebook environment. See [pyspark/VALIDATION.md](pyspark/VALIDATION.md) for runtime limits.

## License

MIT -- see [LICENSE](LICENSE). Each section originally had its own MIT
license file (kept in place for provenance); they're all the same license.
