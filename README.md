# incubyte_assesment# Incubyte TDD Assessment – String Calculator (Python)

A clean, test-driven implementation of the classic **String Calculator** kata following Incubyte's assessment guidelines.

## Tech
- Python 3.10+
- pytest

## Getting started
```bash
# (optional) create and activate a virtualenv
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# install test runner
pip install -e .
pytest -q
```

## Usage
```python
from string_calculator import StringCalculator

calc = StringCalculator()
print(calc.add("1,2,3"))         # 6
print(calc.add("//;\n1;2;1001")) # 3  (numbers > 1000 are ignored)
```

## Requirements covered
1. Empty string returns **0**
2. Single number returns its value
3. Two numbers, comma-delimited returns sum
4. Unknown amount of numbers
5. Newline `\n` as delimiter along with commas
6. Custom delimiter syntax: `//<delim>\n` (e.g., `//;\n1;2`)
7. Negatives are **not allowed** → raise with message listing all negatives
8. Ignore numbers **> 1000**
9. Delimiters of any length: `//[***]\n1***2***3`
10. Multiple delimiters: `//[*][%]\n1*2%3`
11. Multiple delimiters with length: `//[***][%%]\n1***2%%3`

## TDD-friendly commit plan
Use these as incremental commits to showcase your evolution:

1. chore: bootstrap repo (pytest, pyproject, package layout)
2. test: add tests for empty and single number
3. feat: return 0 for empty, parse single number
4. test: two numbers comma-delimited
5. feat: support two numbers
6. test: unknown amount of numbers
7. feat: iterate and sum N numbers
8. test: support newline as delimiter
9. feat: support `\n` delimiter
10. test: custom delimiter `//;\n`
11. feat: parse single custom delimiter
12. test: reject negatives with helpful message
13. feat: raise on negatives listing all negatives
14. test: ignore numbers > 1000
15. feat: ignore > 1000
16. test: delimiters of any length `[***]`
17. feat: support long delimiter in brackets
18. test: multiple delimiters `[x][y]`
19. feat: support multiple delimiters
20. docs: update README with usage and examples

## How to push
```bash
# from project root
git init
git add .
git commit -m "chore: bootstrap repo"
# now follow the commit plan above, making one small change per step
git branch -M main
git remote add origin https://github.com/<your-handle>/incubyte-string-calculator.git
git push -u origin main
```

> After you push, reply to the assessment email with your repository URL.


## CI & Code Quality
- GitHub Actions workflow included: runs pytest and coverage on every push/PR.
- Optional: enable **pre-commit** hooks (Black + Ruff).
```bash
pip install pre-commit
pre-commit install
```

## What to include in your submission email
- Link to the public repo
- Short note on your TDD approach (red → green → refactor)
- **Screenshots**:
  - `pytest` output (all green)
  - `coverage report -m`
  - Git history showing incremental commits
  - (Optional) GitHub Actions green check
