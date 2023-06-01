import unittest

from question2 import Orders

class TestOrders(unittest.TestCase):
    def test_combine_orders(self):
        orders = [70, 30, 10]
        n_max = 100
        expected_orders = 2

        how_many = Orders().combine_orders(orders, n_max)
        assert how_many == expected_orders

        self.assertEqual(how_many, expected_orders)

if __name__ == '__main__':
    unittest.main()