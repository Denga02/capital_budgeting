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

from Area import Area

def main():
    # these values will be given later through a GUI and other methods.
    # variables through input screen
    own_captial = 20000
    outside_captial_type = "funding_amount"
    funding_amount = 10000 
    loan = 1000
    land_type = "property"
    lease_price = 0
    ################################

    # variables through other methods
    initial_investment = 100000
    electricity_feed_yield = 5000
    ################################
    
    # variables that are not defined in the input screen, but are needed.
    own_captial_interest = 0.03
    outside_captial_interest = 0.01
    payout_inflation_rate = 0.015
    deposit_inflation_rate = 0.02
    period = 20

    # in production, create up to 4 surface objects
    area_1 = Area(own_captial, outside_captial_type, funding_amount, loan, land_type, lease_price, initial_investment, electricity_feed_yield, 
                 own_captial_interest, outside_captial_interest, payout_inflation_rate, deposit_inflation_rate, period)
    
    
    if outside_captial_type == "funding_amount":
        print("C_eFÖ_PV: " + str(area_1.npv_funding("pv")))
        print("C_eFÖ_WK: " + str(area_1.npv_funding("wk")))
    else:
        print("dummy")

if __name__ == "__main__":
    main()

