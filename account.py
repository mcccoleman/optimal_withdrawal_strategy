class Account(object):
    def __init__(self, account_type, positions):
        self.account_type = account_type
        self.positions = positions



class RothIRA(Account):
    pass

    def annual_tax_burden(self):
        return 0
    
    def final_liquidation_tax_burden(self):
        return 0

class TraditionalIRA(Account):
    pass

    def annual_tax_burden(self):
        return 0
    
    def final_liquidation_tax_burden(self):
        return 0

def create_roth_ira(positions):
    return RothIRA('Roth_IRA',positions)

print create_roth_ira(['hello'])