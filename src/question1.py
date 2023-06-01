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



