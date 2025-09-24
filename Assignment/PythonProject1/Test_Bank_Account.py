import unittest
from Bank_Account import Account
class TestAccount(unittest.TestCase):

    def test_initial_state(self):
        acc = Account("Samson", 1000)
        self.assertEqual(acc.get_name(), "Samson")
        self.assertEqual(acc.get_balance(), 1000)
        self.assertEqual(acc.get_number(), 8104676967)

    def test_deposit_valid_amount(self):
        acc = Account("Samson", 1000)
        acc.deposit(500)
        self.assertEqual(acc.get_balance(), 1500)

    def test_deposit_negative_amount_raises(self):
        acc = Account("Samson", 1000)
        with self.assertRaises(Exception) as context:
            acc.deposit(-200)
        self.assertEqual(str(context.exception), "Deposit must be positive")

    def test_withdraw_valid_amount(self):
        acc = Account("Samson", 1000)
        acc.withdraw(400)
        self.assertEqual(acc.get_balance(), 600)

    def test_withdraw_insufficient_balance_raises(self):
        acc = Account("Samson", 1000)
        with self.assertRaises(Exception) as context:
            acc.withdraw(2000)
        self.assertEqual(str(context.exception), "Insufficient balance")

    def test_withdraw_negative_amount_raises(self):
        acc = Account("Samson", 1000)
        with self.assertRaises(Exception) as context:
            acc.withdraw(-50)
        self.assertEqual(str(context.exception), "Insufficient balance")

    def test_set_balance_valid(self):
        acc = Account("Samson", 1000)
        acc.set_balance(2000)
        self.assertEqual(acc.get_balance(), 2000)

    def test_set_balance_too_low_raises(self):
        acc = Account("Samson", 1000)
        with self.assertRaises(Exception) as context:
            acc.set_balance(300)
        self.assertEqual(str(context.exception), "Balance must be at least 499")

    def test_set_balance_lower_than_current_raises(self):
        acc = Account("Samson", 1500)
        with self.assertRaises(Exception) as context:
            acc.set_balance(1200)
        self.assertEqual(str(context.exception), "New balance cannot be less than current balance")


if __name__ == "__main__":
    unittest.main()
