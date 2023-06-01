import unittest

from question1 import Contract, Contracts

class TestOrders(unittest.TestCase):
    def test_combine_orders(self):
             
        list_of_contracts = [
            Contract(1, 1),
            Contract(2, 2),
            Contract(3, 3),
            Contract(4, 4),
            Contract(5, 5)
        ]
        renegotiated_contracts = [3]
        top_n = 3

        contracts = Contracts()
        actual_open_contracts = contracts.get_top_N_open_contracts(list_of_contracts, renegotiated_contracts, top_n)

        expected_open_contracts = [5, 4, 2]
        assert expected_open_contracts == actual_open_contracts

if __name__ == '__main__':
    unittest.main()