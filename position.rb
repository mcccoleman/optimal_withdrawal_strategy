class Position
    attr_accessor :share_count, :price_per_share, :ticker_symbol
    def initialize(share_count, price_per_share, ticker_symbol)
        @share_count = share_count
        @price_per_share = price_per_share
        @ticker_symbol = ticker_symbol
    end
end
