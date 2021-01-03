class Account(object):
    def __init__(self, account_type, positions):
        self.account_type = account_type
        self.positions = positions

class RothIRA(Account):
    def __init__(self, positions):
        Account.__init__(self, 'roth_ira', positions)

    def annual_tax_burden(self):
        return 0
    
    def final_liquidation_tax_burden(self):
        return 0

class TraditionalIRA(Account):
    def __init__(self, positions):
        Account.__init__(self, 'trad_ira', positions)

    def annual_tax_burden(self):
        return 0
    
    def final_liquidation_tax_burden(self, ordinary_income_tax_rate):
        account_value = 0
        for position in self.positions:
            account_value += position.current_price * position.number_of_shares

        return account_value - (account_value * ordinary_income_tax_rate)


class Taxable(Account):
    def __init__(self, positions):
        Account.__init__(self, 'taxable', positions)

    def annual_tax_burden(self):
        return 0
    
    def final_liquidation_tax_burden(self):
        return 0


def create_roth_ira(positions):
    return RothIRA(positions)

def create_traditional_ira(positions):
    return TraditionalIRA(positions)

def create_taxable_account(positions):
    return Taxable(positions)