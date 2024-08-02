class Discounting:
    def __init__(self, own_capital, outside_capital_type, funding_amount, loan, own_capital_interest, outside_capital_interest, 
                 period, payout_inflation_rate, deposit_inflation_rate):
        
        self.own_capital = own_capital
        self.outside_capital_type = outside_capital_type
        self.funding_amount = funding_amount
        self.loan = loan
        self.own_capital_interest = own_capital_interest
        self.outside_capital_interest = outside_capital_interest

        self.period = period
        self.payout_inflation_rate = payout_inflation_rate
        self.deposit_inflation_rate = deposit_inflation_rate

    def mixed_costing_interest(self):
        return (((self.own_capital_interest * self.own_capital) + (self.outside_capital_interest * self.loan))
                / (self.own_capital + self.loan))
    
    def discounting_loan_lease(self, costing_interest):
        return (((1 + costing_interest) ** self.period - 1)
                / ((1 + costing_interest) ** self.period * costing_interest))
    
    def discounting_electricity_maintenance(self, costing_interest, inflation_rate):
        return (1 + inflation_rate) * (((1 + costing_interest) ** self.period - (1 + inflation_rate) ** self.period)
                                        / ((1 + costing_interest) ** self.period * (costing_interest - inflation_rate)))