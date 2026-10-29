import ast
import json
from pathlib import Path

def test_all_notebook_python_cells_parse():
    root = Path(__file__).parents[1] / "notebooks"
    paths = list(root.glob("*.ipynb"))
    assert len(paths) == 19
    for path in paths:
        for cell in json.loads(path.read_text())["cells"]:
            if cell["cell_type"] != "code": continue
            source = "\n".join(line for line in "".join(cell["source"]).splitlines() if not line.lstrip().startswith(("!", "%")))
            ast.parse(source)
