"""Local quality checker for the Topic 7 starter.

Checks root Python files and tests/*.py for:
  - syntax errors
  - tab characters
  - trailing whitespace
  - lines longer than 99 characters

Also reports, for top-level functions in root Python files:
  - physical line span
  - number of If nodes
  - deepest nesting of If nodes

The measurements are descriptive only. This tool does not measure
cyclomatic complexity, test coverage or duplication, and it does not
enforce every PEP 8 rule.
"""

import ast
import sys
from pathlib import Path

MAX_LINE_LENGTH = 99
PROJECT_ROOT = Path(__file__).resolve().parent.parent


def files_to_check():
    root_files = sorted(PROJECT_ROOT.glob("*.py"))
    test_files = sorted((PROJECT_ROOT / "tests").glob("*.py"))
    return root_files, test_files


def line_findings(path, text):
    findings = []
    for number, line in enumerate(text.splitlines(), start=1):
        label = f"{path.relative_to(PROJECT_ROOT)}:{number}"
        if "\t" in line:
            findings.append(f"{label}: tab character")
        if line != line.rstrip():
            findings.append(f"{label}: trailing whitespace")
        if len(line) > MAX_LINE_LENGTH:
            findings.append(f"{label}: line has {len(line)} characters (limit {MAX_LINE_LENGTH})")
    return findings


def if_depth(node, depth=0):
    deepest = depth
    for child in ast.iter_child_nodes(node):
        child_depth = depth + 1 if isinstance(child, ast.If) else depth
        deepest = max(deepest, if_depth(child, child_depth))
    return deepest


def function_measurements(path, tree):
    rows = []
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            span = node.end_lineno - node.lineno + 1
            if_nodes = sum(isinstance(n, ast.If) for n in ast.walk(node))
            rows.append(
                f"{path.name}:{node.name}: lines={span}, if_nodes={if_nodes}, "
                f"if_depth={if_depth(node)}"
            )
    return rows


def main():
    root_files, test_files = files_to_check()
    findings = []
    measurements = []
    for path in root_files + test_files:
        text = path.read_text(encoding="utf-8")
        findings.extend(line_findings(path, text))
        try:
            tree = ast.parse(text, filename=str(path))
        except SyntaxError as error:
            findings.append(f"{path.relative_to(PROJECT_ROOT)}:{error.lineno}: syntax error")
            continue
        if path in root_files:
            measurements.extend(function_measurements(path, tree))

    checked = len(root_files) + len(test_files)
    print(f"Checked {checked} file(s).")
    print("Function measurements (descriptive only):")
    for row in measurements:
        print(f"  {row}")
    if findings:
        print(f"{len(findings)} finding(s):")
        for finding in findings:
            print(f"  {finding}")
        return 1
    print("0 findings.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
