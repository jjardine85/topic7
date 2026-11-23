# Requirements: booking summaries

The current code is correct for this contract.
Improve its structure while keeping every point below true.

## Public interface

```
confirmation_summary(reference, quantity, unit_price_pence, is_member)
amendment_summary(reference, quantity, unit_price_pence, is_member)
```

- Keep the module name, function names, parameter names and parameter order.
- Callers may use keyword arguments, so parameter names are part of the contract.

## Inputs

The caller validates inputs before calling. Do not add validation.

- `reference` is a string.
- `quantity` is a positive integer.
- `unit_price_pence` is a non-negative integer.
- `is_member` is a Boolean.
- For an amendment, `quantity` is the new TOTAL number of places, not a change.

## Pricing policy

- Subtotal = quantity x unit price, in whole pence.
- Members booking at least four places get 10% off the subtotal, rounded down to a whole penny.
- Non-members get no discount.
- Both summary functions deliberately use the same pricing policy.

## Output

Return the exact string. Keep the reference unchanged. Keep the word `places` even for one place.

```
Confirmed {reference}: {quantity} places; total {total_pence} pence.
Amended {reference}: {quantity} places; total {total_pence} pence.
```

The functions must not print, write files or make external calls.

## Worked examples

| Case | Inputs | Total |
| --- | --- | --- |
| Member below threshold | 3 places at 100p | 300 pence |
| Member at threshold | 4 places at 100p | 360 pence |
| Non-member at threshold | 4 places at 100p | 400 pence |
| Rounding | Member, 4 places at 101p | 363 pence |
| Zero price | Member, 4 places at 0p | 0 pence |

## Out of scope

New discounts, input validation, saving data and notifications are all out of scope.
Internal helper functions are allowed.
