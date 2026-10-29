import ast
from itertools import combinations
import json
from pathlib import Path
import random

ROOT = Path(__file__).parents[1]

def functions(file):
    ns = {}
    for cell in json.loads((ROOT / file).read_text())["cells"]:
        if cell["cell_type"] != "code":
            continue
        tree = ast.parse("".join(cell["source"]))
        defs = [node for node in tree.body if isinstance(node, (ast.FunctionDef, ast.ClassDef))]
        exec(compile(ast.Module(defs, type_ignores=[]), file, "exec"), ns)
    return ns

def test_countx_empty_duplicates_and_boundaries():
    count = functions("binary_search.ipynb")["countx"]
    for seq in ([], [1], [1, 2, 2, 3]):
        for x in range(5):
            assert count(seq, x) == seq.count(x)

def test_pair_count_matches_brute_force_including_negative_k():
    count = functions("prefix_sums_and_two_pointers.ipynb")["count_pairs_with_difference_greater_than_k"]
    rng = random.Random(0)
    for _ in range(100):
        seq = sorted(rng.choices(range(-3, 4), k=rng.randrange(8)))
        for k in range(-3, 5):
            assert count(seq, k) == sum(seq[j] - seq[i] > k for i in range(len(seq)) for j in range(i + 1, len(seq)))

def test_coherent_team_matches_all_subsets():
    best = functions("prefix_sums_and_two_pointers.ipynb")["best_team_sum"]
    rng = random.Random(0)
    assert best([1, 3, 5, 2, 4, 6]) == 18
    for _ in range(100):
        seq = rng.choices(range(6), k=rng.randrange(8))
        expected = 0
        for size in range(len(seq) + 1):
            for team in combinations(seq, size):
                ordered = sorted(team)
                if size < 3 or ordered[0] + ordered[1] >= ordered[-1]:
                    expected = max(expected, sum(team))
        assert best(seq) == expected
