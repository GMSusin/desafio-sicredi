class Contract:
    def __init__(self, id, debt):
        self.id = id
        self.debt = debt

    def __str__(self):
        return 'id={}, debt={}'.format(self.id, self.debt)


class Contracts:
    def get_top_N_open_contracts(self, open_contracts, renegotiated_contracts, top_n):
        filtered_contracts = [c for c in open_contracts if c.id not in renegotiated_contracts]
        sorted_contracts = sorted(filtered_contracts, key=lambda x: x.debt, reverse=True)
        return [c.id for c in sorted_contracts[:top_n]]

           
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
print("actual_open_contracts", actual_open_contracts)
expected_open_contracts = [5, 4, 2]
assert expected_open_contracts == actual_open_contracts
