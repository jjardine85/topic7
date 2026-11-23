# Activity 2: refactor in small steps (20 minutes)

Swap roles. Partner B implements. Partner A checks the plan and questions the reasoning.
Start from the passing tests you committed in Activity 1.

## Steps

1. Confirm the concern, the benefit you expect and the scope.
2. Make one coherent structural change.
   If you extract the pricing calculation, give the helper a clear name and explicit inputs.
   Keep the results in whole pence.
3. Update one caller and run the tests. Then update the second caller and run them again.
4. Keep public signatures, keyword parameter names and exact returned text the same.
5. Improve names and conditions where you can justify it.
   Do not change the policy, the rounding or the output format.
6. Look at the whole change, including any new files. Run the full checks.

## Commands

```
python3 -m unittest discover -s tests -v
python3 tools/check_quality.py
python3 example.py
git status
git diff
git add booking.py
git diff --cached
git commit -m "Centralise shared booking pricing without changing summaries"
git rev-parse HEAD
```

`git diff` does not show new untracked files. Open them as well, and stage any new helper file by name.
Use a commit message that matches what you actually changed.

If a check fails, find the cause before you edit anything else.
Never weaken an expected result just to make a test pass.

**Stretch:** would a separate module, a named constant for the discount or a different structure help? Explain the trade-off. You do not need to build every option.

## Common traps

- `quantity > 4` removes the discount at exactly four places.
- `round(subtotal * 0.9)` changes the rounding. Four places at 101p must cost 363 pence.
- Discounting the unit price first changes the result. Discount the subtotal.
- Leaving a second copy of the rule in one caller.
- Renaming a public parameter breaks keyword callers.
- Changing `places` to `place` or tidying the reference changes the required output.
