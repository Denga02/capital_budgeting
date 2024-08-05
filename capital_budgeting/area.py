from typing import Any


class Area:
    def __init__(self, own_captial, outside_captial_type, funding_amount, loan, land_type, lease_price, initial_investment, electricity_feed_yield, 
                 own_captial_interest, outside_captial_interest, payout_inflation_rate, deposit_inflation_rate, period):
        
        self.own_captial = own_captial
        self.outside_captial_type = outside_captial_type
        self.funding_amount = funding_amount
        self.loan = loan
        self.land_type = land_type
        self.lease_price = lease_price
        self.initial_investment = initial_investment
        self.electricity_feed_yield = electricity_feed_yield
        self.own_captial_interest = own_captial_interest
        self.outside_capital_interest = outside_captial_interest
        self.payout_inflation_rate = payout_inflation_rate
        self.deposit_inflation_rate = deposit_inflation_rate
        self.period = period

    # calculation of mixed costing interest through own_capital_interest (i_EK) and outside_capital_interest (i_FK)
    def mixed_costing_interest(self):
        return ( (((self.own_captial_interest * self.own_captial) + (self.outside_capital_interest * self.loan)))
                / (self.own_captial + self.loan) 
            )

    # costs for maintenance (A_Wartung)
    # powertype must be pv or wk
    def a_maintaince(self, powertype):
        if powertype == "pv":
            return 0.025 * self.initial_investment
        if powertype == "wk":
            return 0.05 * self.initial_investment

    # net present value method one-off funding
    def npv_funding(self, powertype, discounting, discounted_calculations):
        costing_interest = self.own_captial_interest
        
        return ((self.initial_investment * (-1) ) 
                - discounted_calculations.calculate_discounted_lease(costing_interest, discounting)
                + self.own_captial + self.funding_amount  
                + discounted_calculations.calculate_discounted_electricity_feed_yield(costing_interest, discounting) 
                - discounted_calculations.calculate_discounted_maintaince(powertype, costing_interest, discounting)
                )

    # Net present value method for loan
    def npv_loan(self, powertype, discounting, discounted_calculations):
        costing_interest = self.mixed_costing_interest()
        return ((self.initial_investment * (-1) ) 
                - discounted_calculations.calculate_discounted_lease(costing_interest, discounting)
                + self.own_captial + discounted_calculations.calculate_discounted_loan(costing_interest, discounting) 
                + discounted_calculations.calculate_discounted_electricity_feed_yield(costing_interest, discounting)
                - discounted_calculations.calculate_discounted_maintaince(powertype, costing_interest, discounting)
                )


