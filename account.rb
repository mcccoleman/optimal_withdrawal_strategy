class Account
    attr_accessor :positions
    def initialize(positions)
        @positions = positions
    end

    def add_position(position)
        @positions.push(position)
    end

    def position_count
        @positions.length
    end
end

class RothIRA < Account
    attr_accessor :positions, :account_type
    def initialize(positions)
        super(positions)
        @account_type = 'Roth IRA'
    end
end
