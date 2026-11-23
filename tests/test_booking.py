"""Initial tests for the booking summaries."""

import unittest

from booking import amendment_summary, confirmation_summary


class ConfirmationSummaryTests(unittest.TestCase):

    def test_member_with_five_places_gets_discount(self):
        self.assertEqual(
            confirmation_summary("BK100", 5, 100, True),
            "Confirmed BK100: 5 places; total 450 pence.",
        )

    def test_non_member_pays_full_price(self):
        self.assertEqual(
            confirmation_summary("BK200", 5, 100, False),
            "Confirmed BK200: 5 places; total 500 pence.",
        )

    def test_member_with_large_booking(self):
        self.assertEqual(
            confirmation_summary("BK300", 10, 20, True),
            "Confirmed BK300: 10 places; total 180 pence.",
        )


class AmendmentSummaryTests(unittest.TestCase):

    def test_member_with_two_places_has_no_discount(self):
        self.assertEqual(
            amendment_summary("BK100", 2, 100, True),
            "Amended BK100: 2 places; total 200 pence.",
        )

    def test_non_member_pays_full_price(self):
        self.assertEqual(
            amendment_summary("BK400", 6, 50, False),
            "Amended BK400: 6 places; total 300 pence.",
        )

    def test_member_with_five_places_gets_discount(self):
        self.assertEqual(
            amendment_summary("BK500", 5, 100, True),
            "Amended BK500: 5 places; total 450 pence.",
        )


if __name__ == "__main__":
    unittest.main()
