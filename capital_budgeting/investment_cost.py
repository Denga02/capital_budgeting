class InvestmentCost:
    def __init__(self, initial_investment, land_type, lease_price, electricity_feed_yield):
        self.initial_investment = initial_investment
        self.land_type = land_type
        self.lease_price = lease_price
        self.electricity_feed_yield = electricity_feed_yield
    
    def maintenance_cost(self, power_type):
        if power_type == "pv":
            return 0.025 * self.initial_investment
        elif power_type == "wk":
            return 0.05 * self.initial_investment
        else:
            raise ValueError("Unknown power type")
        
