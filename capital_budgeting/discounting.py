class DiscountingFactor:
    def discounting_loan_lease(self, costing_interest, period):
        return (((1 + (costing_interest))**(period) - 1) 
                / ((1 + costing_interest )**(period) * costing_interest))
    
    def discounting_electricity_maintance(self, costing_interest, inflation_type, period):
        return (1 + inflation_type ) * (((1 + (costing_interest))**(period) - (1 + inflation_type)**(period)) 
                                        / ((1 + costing_interest)**(period) * (costing_interest - inflation_type)))

class DiscountedCalculations:
    def __init__(self, area):
        self.area = area
    
    def calculate_discounted_electricity_feed_yield(self, costing_interest, discounting):
        return self.area.electricity_feed_yield * discounting.discounting_electricity_maintance(costing_interest, self.area.deposit_inflation_rate, self.area.period)
    
    def calculate_discounted_maintaince(self, powertype, costing_interest, discounting):
        return self.area.a_maintaince(powertype) * discounting.discounting_electricity_maintance(costing_interest, self.area.payout_inflation_rate, self.area.period)
    
    def calculate_discounted_lease(self, costing_interest, discounting):
        return self.area.lease_price * discounting.discounting_loan_lease(costing_interest, self.area.period)
    
    def calculate_discounted_loan(self, costing_interest, discounting):
        return self.area.loan * discounting.discounting_loan_lease(costing_interest, self.area.period)