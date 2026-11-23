# Activity 1: evaluate and protect behaviour (20 minutes)

Partner A drives. Partner B challenges assumptions and records findings.
Work against the unchanged `booking.py`.

## Steps

1. Read both functions, `docs/requirements.md` and the caller in `example.py`.
2. Use `docs/quality-checklist.md` to find at least two concrete quality concerns.
3. Choose one improvement. Say which maintenance task it should make easier.
   Centralising the shared pricing rule is a suitable scope.
4. Fill in the concerns and plan sections of `docs/refactoring-plan.md`.
5. Create `tests/test_boundaries.py`. Use `unittest` and the two public functions.
   Use `tests/test_booking.py` as a model.
6. Test both summary functions. Think about:
   - a member below the threshold and at the threshold
   - a non-member at the threshold
   - rounding
   - zero price
   - keyword arguments
   - exact text, including the reference and the word `places`
7. Work out each expected string from the requirements. Do not call the code to get the answer.
8. Run the checks. Your new tests should pass against the unchanged code.
   If one fails, find out why before you go further.

## Commands

```
python3 -m unittest discover -s tests -v
python3 tools/check_quality.py
git diff
git add tests
git diff --cached
git commit -m "Protect booking summary behaviour before refactoring"
git rev-parse HEAD
git status
```

Only commit work you actually did. Save your plan and notes too.

A failing test here might mean a wrong expectation, an import error or an accidental edit. Find the cause.

**Stretch:** which mistakes could tests of a pricing helper alone miss at the caller boundary?

Save your work before the break.
