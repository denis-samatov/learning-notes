import ast
import contextlib
import io
import json
from pathlib import Path
import random
import numpy as np
from deap import base, creator, tools, algorithms

ROOT = Path(__file__).parents[1]

def run(file):
    ns = dict(base=base, creator=creator, tools=tools, algorithms=algorithms, random=random, np=np)
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    ns["plt"] = plt
    old_show = plt.show
    plt.show = lambda: None
    try:
        for cell in json.loads((ROOT / file).read_text())["cells"]:
            if cell["cell_type"] != "code": continue
            source = "".join(cell["source"])
            if any(line.lstrip().startswith(("!", "%")) for line in source.splitlines()): continue
            with contextlib.redirect_stdout(io.StringIO()): exec(source, ns)
    finally:
        plt.show = old_show
        plt.close("all")
    return ns

def test_scalar_fitness_contract():
    file = "genetic_algorithm_2.ipynb"
    ns = {"np": np}
    for cell in json.loads((ROOT / file).read_text())["cells"]:
        if cell["cell_type"] != "code": continue
        try: tree = ast.parse("".join(cell["source"]))
        except SyntaxError: continue
        defs = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "minFunction"]
        if defs: exec(compile(ast.Module(defs, type_ignores=[]), file, "exec"), ns)
    fitness = ns["minFunction"]([0.0])
    assert isinstance(fitness[0], (int, float, np.floating))
    assert fitness == (4.0,)

def test_seeded_runs_recover_known_minima_and_repeat():
    for file, minimum in [("genetic_algorithm_1.ipynb", 0.0), ("genetic_algorithm_2.ipynb", 4.0)]:
        first, second = run(file), run(file)
        a, b = list(first["hof"][0]), list(second["hof"][0])
        assert a == b
        assert all(-5 <= x <= 5 for x in a)
        assert abs(first["minFunction"](a)[0] - minimum) < 0.02
