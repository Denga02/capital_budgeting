#######################################################################
__author__ = "Danny Baumgardt"
__copyright__ = "Copyright 2024, Danny Baumgardt"
__license__ = "CC BY-NC 4.0"
__version__ = 0.1 
__GitHub__ = "https://github.com/Denga02/capital_budgeting/tree/main"
__status__ = "Development"
#######################################################################

##############################################################
### Information about the variables for the using formulas ###
##  formulars are saved in ...                              ##
#                                                            #
#   own_captial                 (E_EK)                       #
#   funding_amount              (E_eFÖ)                      #
#   loan                        (E_FÖD)                      #
#   initial_investment          (A_0)                        #
#   electricity_feed_yield      (E_Strom)                    #
#   own_captial_interest        (i_EK)                       #
#   outside_captial_interest    (i_FK)                       #
#   payout_inflation_rate       (e_A)                        #
#   deposit_inflation_rate      (e_E)                        #
#   period                      (n)                          #
##############################################################

from area import AreaCalculation

def main():
    # Beispielwerte für die Parameter
    own_capital = 100000
    outside_capital_type = "Loan"
    funding_amount = 50000
    loan = 150000
    own_capital_interest = 0.03
    outside_capital_interest = 0.05
    initial_investment = 200000
    land_type = "Agricultural"
    lease_price = 10000
    electricity_feed_yield = 15000
    period = 20
    payout_inflation_rate = 0.02
    deposit_inflation_rate = 0.01
    power_type = "pv"  # Beispiel: "pv" für Photovoltaik

    # Instanziiere die Hauptklasse
    area_1 = AreaCalculation(
        own_capital, outside_capital_type, funding_amount, loan, own_capital_interest,
        outside_capital_interest, initial_investment, land_type, lease_price, electricity_feed_yield,
        period, payout_inflation_rate, deposit_inflation_rate
    )

    print("Ergebnisse der Berechnungen:")
    print(f"NPV Funding: {area_1.npv_funding}")
    print(f"NPV Loan: {area_1.npv_loan}")

# Aufruf der Main-Methode
if __name__ == "__main__":
    main()