# Setup and baseline

On Windows use `py` in place of `python3` in every command.

## 1. Check your tools

```
python3 --version
git --version
```

You need Python 3.9 or later and Git.

## 2. Run the baseline checks

Open a terminal inside the `topic7-starter` folder.

```
python3 -m unittest discover -s tests -v
python3 tools/check_quality.py
python3 example.py
```

Expected: six passing tests, `0 findings.` and these two lines:

```
Confirmed BK100: 5 places; total 450 pence.
Amended BK100: 2 places; total 200 pence.
```

Write down what you actually saw. Do not copy the expected results as if you observed them.

## 3. Make the baseline commit

Use a fresh extracted folder that is not inside another Git repository.
Run `git status` first. It should say this is not a Git repository.
If it names a parent repository, move the folder somewhere else or ask your tutor.

```
git init
git config user.name
git config user.email
```

If either value is missing, set it for this repository only:

```
git config user.name "YOUR NAME"
git config user.email "YOUR APPROVED EMAIL"
```

Then commit, tag and branch:

```
git add .
git commit -m "Establish Topic 7 baseline"
git branch -M main
git tag workshop-start
git switch -c refactor/booking-quality
git rev-parse HEAD
git status
```

Keep the `workshop-start` tag unchanged. Your working tree should now be clean.
Record the commit identifier in `docs/evidence-log.md`.

## If you get stuck

- **Import error:** check you are inside `topic7-starter` and use the exact command with `-s tests`.
- **Zero tests found:** check `tests/test_booking.py` exists. Zero tests is not a pass.
- **Python command missing:** use `py` on Windows, or ask your tutor to check the installation.
- **Baseline failure:** stop and investigate before changing code or tests.
- **Missing Git identity:** set your own name and approved email locally (step 3).
- **Unexpected changes:** run `git status` and `git diff`, and save your work before switching branch.
- **Need the original code:** run `git show workshop-start:booking.py` or extract the ZIP again.
- **Git not available:** keep named before and after copies outside the project, save your results, and mark the commit steps as not performed.

Do not use `git reset --hard`, force pushes or anything that overwrites work you cannot explain.
