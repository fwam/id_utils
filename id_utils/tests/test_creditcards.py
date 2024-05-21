import unittest
from id_utils import CreditCard

class TestCC(unittest.TestCase):
    def test_validation(self):
        # Valid MasterCard
        self.assertIsNotNone(CreditCard("5425233430109903"))
        # Valid VISA
        self.assertIsNotNone(CreditCard("4000000000001000"))
        # Invalid card (length)
        with self.assertRaises(ValueError):
            CreditCard("2137420")
            CreditCard("634352082081226361615")
