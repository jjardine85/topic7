# Peer review (15 minutes)

Another pair reviews your change if possible. If not, walk through it together as partners.
Record the method you actually used.

```
git diff workshop-start..HEAD
git status
```

## Review questions

1. Can the reviewer find the shared pricing rule and explain how both callers use it?
2. Does the full diff keep the interfaces, caller arguments and exact output?
3. Do the tests check the threshold, membership, rounding and caller behaviour?
4. Have any expected results been weakened, or useful tests removed?
5. Does any new helper make the stated maintenance task easier? What trade-off remains?
6. Hypothetical: if the discount changed to 15%, how many places would you edit now?

## Record

**Reviewer, method and commit reviewed:**

**Feedback, with the requirement or quality point it relates to:**

**Author response, any revision and the checks you ran after it:**

**Decision and reasons, including anything unresolved:**

A reasoned approval is fine. Do not invent a problem to fill this record.

## Optional: local integration

Only do this when all corrections are committed and `git status` is clean.

```
git switch main
git merge --ff-only refactor/booking-quality
python3 -m unittest discover -s tests -v
python3 tools/check_quality.py
git rev-parse HEAD
git status
```

This is a local fast-forward with no merge commit and no hosted checks.
If Git refuses, ask your tutor. Do not force it.
If your work is not finished, keep it on the branch and record integration as not performed.
