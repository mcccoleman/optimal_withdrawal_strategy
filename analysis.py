from account import create_roth_ira
from account import create_traditional_ira
from account import create_taxable_account
from position import create_position

positions = [create_position('XOM', 100, 100, 0, 0), create_position('AAPL', 100, 100, 0, 0), create_position('TSLA', 100, 100, 0, 0), create_position('AAPL', 100, 100, 0, 0)]
trad = create_traditional_ira(positions)

print trad.final_liquidation_tax_burden(0.25)