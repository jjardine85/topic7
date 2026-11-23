"""Example caller for the booking summaries."""

from booking import amendment_summary, confirmation_summary


def main():
    print(confirmation_summary("BK100", 5, 100, True))
    print(amendment_summary(reference="BK100", quantity=2, unit_price_pence=100, is_member=True))


if __name__ == "__main__":
    main()
