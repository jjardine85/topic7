# Topic 7 starter: code quality and safe refactoring

Professional Software Practices, Topic 7.

This folder holds a small booking component that works correctly.
Your job is to evaluate it, add tests that protect its behaviour, and then improve its structure without changing what it does.

## What is in this folder

| File or folder | What it is |
| --- | --- |
| `booking.py` | The booking component. Two public functions build summary text. |
| `example.py` | A caller that uses both functions. |
| `tests/test_booking.py` | Six starting tests. They all pass. |
| `tools/check_quality.py` | A local checker for style rules and simple function measurements. |
| `docs/requirements.md` | The contract the code must keep. Read this first. |
| `docs/activity-1.md` | Activity 1: evaluate and protect behaviour. |
| `docs/activity-2.md` | Activity 2: refactor in small steps. |
| `docs/quality-checklist.md` | Questions to guide your evaluation. |
| `docs/refactoring-plan.md` | Plan to complete before you change the code. |
| `docs/peer-review.md` | Prompts for the peer review. |
| `docs/evidence-log.md` | Record of your actual results and contribution. |
| `SETUP.md` | Setup, baseline commit and troubleshooting. |

## Quick start

Open a terminal inside this folder. On Windows use `py` in place of `python3`.

```
python3 -m unittest discover -s tests -v
python3 tools/check_quality.py
python3 example.py
```

You should see six passing tests, zero checker findings and this output:

```
Confirmed BK100: 5 places; total 450 pence.
Amended BK100: 2 places; total 200 pence.
```

Then follow `SETUP.md` to make your baseline commit.

You need Python 3.9 or later, Git and an editor.
No packages or online accounts are needed.
