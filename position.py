class Position(object):
    def __init__(self, current_price, cost_basis, dividend_distribution, percentage_qualified_dividend):
        self.current_price = current_price
        self.cost_basis = cost_basis
        self.dividend_distribution = dividend_distribution
        self.percentage_qualified_dividend = percentage_qualified_dividend
