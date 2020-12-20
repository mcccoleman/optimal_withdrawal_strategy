require './account.rb'
require './position.rb'


first_position = Position.new(2, 100, 'AAPL')
second_position = Position.new(2, 100, 'AAPL')



account = RothIRA.new([first_position])

account.add_position(second_position)

print account.position_count
print account.account_type

