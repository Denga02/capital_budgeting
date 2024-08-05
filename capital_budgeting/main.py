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

from area import Area
from discounting import DiscountedCalculations, DiscountingFactor

def main():
    # Standardwerte für die Erstellung der Area-Objekte
    default_values = {
        "own_captial": 20000,
        "outside_captial_type": "funding_amount",
        "funding_amount": 10000,
        "loan": 1000,
        "land_type": "property",
        "lease_price": 0,
        "initial_investment": 100000,
        "electricity_feed_yield": 5000,
        "own_captial_interest": 0.03,
        "outside_captial_interest": 0.01,
        "payout_inflation_rate": 0.015,
        "deposit_inflation_rate": 0.02,
        "period": 20
    }

    # Erstellung von 4 Area-Objekten mit den Standardwerten
    areas = [Area(**default_values) for _ in range(4)]

    # Erstellung von Instanzen der Klassen Discounting und DiscountedCalculations
    Discounting_factor = DiscountingFactor()

    # Berechnungen für jedes Area-Objekt durchführen
    for index, area in enumerate(areas):
        discounted_calculations = DiscountedCalculations(area)
        
        print(f"Berechnungen für Area {index + 1}:")
        if area.outside_captial_type == "funding_amount":
            print("C_eFÖ_PV: " + str(area.npv_funding("pv", Discounting_factor, discounted_calculations)))
            print("C_eFÖ_WK: " + str(area.npv_funding("wk", Discounting_factor, discounted_calculations)))
        else:
            print("C_FÖD_PV: " + str(area.npv_loan("pv", Discounting_factor, discounted_calculations)))
            print("C_FÖD_WK: " + str(area.npv_loan("wk", Discounting_factor, discounted_calculations)))
        print("-" * 30)

if __name__ == "__main__":
    main()
