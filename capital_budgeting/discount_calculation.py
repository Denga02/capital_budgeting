from investment_cost import InvestmentCost

class DiscountCalculation:
    def __init__(self, financial_details, investment_details, discount_calculations):
        self.financial_details = financial_details
        self.investment_details = investment_details
        self.discount_calculations = discount_calculations
    
    def calculate_discounted_electricity_feed_yield(self, costing_interest):
        return self.investment_details.electricity_feed_yield * \
               self.discount_calculations.discounting_electricity_maintenance(costing_interest, 
                                                                              self.discount_calculations.deposit_inflation_rate)
    
    def calculate_discounted_maintenance(self, power_type, costing_interest):
        return self.investment_details.maintenance_cost(power_type) * \
               self.discount_calculations.discounting_electricity_maintenance(costing_interest, 
                                                                              self.discount_calculations.payout_inflation_rate)
    
    def calculate_discounted_lease(self, costing_interest):
        return self.investment_details.lease_price * \
               self.discount_calculations.discounting_loan_lease(costing_interest)
    
    def calculate_discounted_loan(self, costing_interest):
        return self.financial_details.loan * \
               self.discount_calculations.discounting_loan_lease(costing_interest)