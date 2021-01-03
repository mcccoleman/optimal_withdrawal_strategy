class Position(object):
    def __init__(self, ticker, cost_basis, number_of_shares, dividend_distribution_yield, percentage_qualified_dividend):
        self.ticker = ticker
        self.cost_basis = cost_basis
        self.current_price = cost_basis
        self.number_of_shares = number_of_shares
        self.dividend_distribution_yield = dividend_distribution_yield
        self.percentage_qualified_dividend = percentage_qualified_dividend

    def update_current_price(self, current_price):
        self.current_price = current_price

    def gain_or_loss(self):
        return (self.current_price - self.cost_basis) * self.number_of_shares

def create_position(ticker, cost_basis, number_of_shares, dividend_distribution_yield, percentage_qualified_dividend):
    return Position(ticker, cost_basis, number_of_shares, dividend_distribution_yield, percentage_qualified_dividend)
