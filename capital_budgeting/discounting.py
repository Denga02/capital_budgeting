class Discounting:

    # calculation of the discount rate for loans and leases
    def discounting_loan_lease(self, costing_interest, period):
        return (((1 + (costing_interest))**(period) - 1) 
                / ((1 + costing_interest )**(period) * costing_interest))
    
    # calculation of the discount rate for electricity and maintenance
    # use deposit_inflation_rate e_E for electricity
    # use deposit_inflation_rate e_A for maintenance
    def discounting_electricity_maintance(self, costing_interest, inflation_type, period):
        return (1 + inflation_type ) * (((1 + (costing_interest))**(period) - (1 + inflation_type)**(period)) 
                                        / ((1 + costing_interest)**(period) * (costing_interest - inflation_type)))

class DiscountedCalculations:
    def __init__(self, area):
        self.area = area
    
    # amount of the discounted_electricity_feed_yield E_Strom * d_Strom
    def calculate_discounted_electricity_feed_yield(self, costing_interest, discounting):
        return self.area.electricity_feed_yield * discounting.discounting_electricity_maintance(costing_interest, self.area.deposit_inflation_rate, self.area.period)
    
    # amount of the discounted maintenance cost A_Wartung * d_Wartung
    def calculate_discounted_maintaince(self, powertype, costing_interest, discounting):
        return self.area.a_maintaince(powertype) * discounting.discounting_electricity_maintance(costing_interest, self.area.payout_inflation_rate, self.area.period)
    
    # amount of the discounted lease cost A_Pacht * d_Pacht
    def calculate_discounted_lease(self, costing_interest, discounting):
        return self.area.lease_price * discounting.discounting_loan_lease(costing_interest, self.area.period)
    
    # amount of the discounted loan  E_FÖD * d_FÖD
    def calculate_discounted_loan(self, costing_interest, discounting):
        return self.area.loan * discounting.discounting_loan_lease(costing_interest, self.area.period)