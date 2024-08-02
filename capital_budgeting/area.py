from discount_calculation import DiscountCalculation
from investment_cost import InvestmentCost
from discounting import Discounting


class AreaCalculation:
    def __init__(self, own_capital, outside_capital_type, funding_amount, loan, own_capital_interest,
                 outside_capital_interest, initial_investment, land_type, lease_price, electricity_feed_yield,
                 period, payout_inflation_rate, deposit_inflation_rate):
        
        # Instanziiere Investitionsdetails
        # investment_details
        self.investment_cost = InvestmentCost(initial_investment, land_type, lease_price, electricity_feed_yield)
        # Instanziiere Diskontierungsberechnungen
        # discount_calcutlation
        self.discount = Discounting(own_capital, outside_capital_type, funding_amount, loan, own_capital_interest, outside_capital_interest, 
                                    period, payout_inflation_rate, deposit_inflation_rate)
        # Instanziiere Ertragsberechnungen
        # yield
        self.discount_calculations = DiscountCalculation(self.investment_cost, self.discount)
    
    def npv_funding(self, power_type):
        costing_interest = self.discount.own_capital_interest
        return ( self.investment_cost.initial_investment * -1
                 - self.discount_calculations.calculate_discounted_lease(costing_interest)
                 + self.discount.own_capital
                 + self.discount.funding_amount
                 + self.discount_calculations.calculate_discounted_electricity_feed_yield(costing_interest)
                 - self.discount_calculations.calculate_discounted_maintenance(power_type, costing_interest))
    
    def npv_loan(self, power_type):
        costing_interest = self.financial_details.mixed_costing_interest()
        return (self.investment_details.initial_investment * -1
                - self.yield_calculations.calculate_discounted_lease(costing_interest)
                + self.financial_details.own_capital
                + self.yield_calculations.calculate_discounted_loan(costing_interest)
                + self.yield_calculations.calculate_discounted_electricity_feed_yield(costing_interest)
                - self.yield_calculations.calculate_discounted_maintenance(power_type, costing_interest))


