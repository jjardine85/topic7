"""Booking summaries for validated booking inputs."""


def confirmation_summary(reference, quantity, unit_price_pence, is_member):
    """Return the confirmation text for a booking."""
    q = quantity
    p = unit_price_pence
    m = is_member
    x = q * p
    if m:
        if q >= 4:
            x = x * 90 // 100
    return "Confirmed " + reference + ": " + str(q) + " places; total " + str(x) + " pence."


def amendment_summary(reference, quantity, unit_price_pence, is_member):
    """Return the amendment text for a booking."""
    q = quantity
    p = unit_price_pence
    m = is_member
    x = q * p
    if m:
        if q >= 4:
            x = x * 90 // 100
    return f"Amended {reference}: {q} places; total {x} pence."
