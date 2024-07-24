class Area:
    def __init__(self, own_captial, outside_captial_type, funding_amount, loan, land_type, lease_price, initial_investment, electricity_feed_yield, 
                 own_captial_interest, outside_captial_interest, payout_inflation_rate, deposit_inflation_rate, period ):
        
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
    
    # calculation of the discount rate for loans and leases
    def discounting_loan_lease(self, costing_interest):
        return (((1 + (costing_interest))**(self.period) - 1) 
                / ((1 + costing_interest )**(self.period) * costing_interest))
    
    # calculation of the discount rate for electricity and maintenance
    # use deposit_inflation_rate e_E for electricity
    # use deposit_inflation_rate e_A for maintenance
    def discounting_electricity_maintance(self, costing_interest, inflation_type):
        return (1 + inflation_type ) * (((1 + (costing_interest))**(self.period) - (1 + inflation_type)**(self.period)) 
                                        / ((1 + costing_interest)**(self.period) * (costing_interest - inflation_type)))
    
    # costs for maintenance (A_Wartung)
    # powertype must be pv or wk
    def a_maintaince(self, powertype):
        if powertype == "pv":
            return 0.025 * self.initial_investment
        if powertype == "wk":
            return 0.05 * self.initial_investment
        
    # amount of the discounted_electricity_feed_yield E_Strom * d_Strom
    def calculate_discounted_electricity_feed_yield(self, costing_interest):
        return self.electricity_feed_yield * self.discounting_electricity_maintance(costing_interest, self.deposit_inflation_rate)
    
    # amount of the discounted maintenance cost A_Wartung * d_Wartung
    def calculate_discounted_maintaince(self, powertype, costing_interest):
        return self.a_maintaince(powertype) * self.discounting_electricity_maintance(costing_interest, self.payout_inflation_rate)
    
    # amount of the discounted lease cost A_Pacht * d_Pacht
    def calculate_discounted_lease(self, costing_interest):
        return self.lease_price * self.discounting_loan_lease(costing_interest)
    
    # amount of the discounted loan  E_FÖD * d_FÖD
    def calculate_discounted_loan(self, costing_interest):
        return self.loan * self.discounting_loan_lease(costing_interest)
    
    # net present value method one-off funding
    def npv_funding(self, powertype):
        costing_interest = self.own_captial_interest
        return ((self.initial_investment * (-1) ) - self.calculate_discounted_lease(costing_interest)
                + self.own_captial + self.funding_amount  
                + self.calculate_discounted_electricity_feed_yield(costing_interest) 
                - self.calculate_discounted_maintaince(powertype, costing_interest)
                )
    # Net present value method for loan
    def npv_loan(self, powertype):
        costing_interest = self.mixed_costing_interest()
        return ((self.initial_investment * (-1) ) - self.calculate_discounted_lease(costing_interest)
                + self.own_captial + self.calculate_discounted_loan(costing_interest) 
                + self.calculate_discounted_electricity_feed_yield(costing_interest)
                - self.calculate_discounted_maintaince(powertype, costing_interest)
                )

    

