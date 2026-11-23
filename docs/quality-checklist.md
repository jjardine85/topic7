# Quality checklist

For each question, record one of: a concern, no concern found, or not assessed.
A short function or a clean checker report is not enough evidence of quality on its own.

## Readability and standards

- Do names show purpose, units and meaning?
- Can you find the pricing rule quickly?
- Are conditions easy to follow?
- Is this a supported concern or a personal preference?

## Responsibilities and dependencies

- Does each function have one clear job?
- Are inputs and dependencies explicit?
- Would a helper make the design clearer, or just add more places to look?

## Duplication and complexity

- Is the same rule kept in more than one place?
- How many places would you edit for one policy change?
- Does the similar code represent shared knowledge, or two policies that change separately?
- Can you follow the control flow across the whole affected area, including any helpers?

## Behaviour and verification

- Which return values, interfaces and exact text must stay the same?
- Which requirements do the current tests check? Which do they miss?
- Do the tests check the callers as well as any helper?
- Did you run the baseline checks and link the results to a commit?

## A useful finding has three parts

1. **Location:** file and function.
2. **Observation:** what you can see in the code.
3. **Consequence:** which maintenance task this makes harder.
