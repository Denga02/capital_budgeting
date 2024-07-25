# capital_budgeting

## Function
- calculate captial profitability according to the Net present value method for wind power or photovoltaics
- use the following formulas:
  - with one-off funding as outside captial  
  $C_{Strom} = -A_0 - A_{Pacht} * d_{Pacht} + E_{EK} + E_{eFÖD} + E_{Strom} * d_{Strom} - A_{Wartung} * d_{Wartung}$
  - with loan as outside captial   
  $C_{Strom} = -A_0 - A_{Pacht} * d_{Pacht} + E_{EK} + E_{FÖD} * d_{eFÖD} + E_{Strom} * d_{Strom} - A_{Wartung} * d_{Wartung}$
- detailed discounting formula  
  $d_{FÖD} = (\frac{(1 + i)^n -1}{(1+i)^n*i})$  

  $d_{Pacht} = (\frac{(1+i)^n-1}{(1+i)^n*i})$

  $d_{Strom} = (1+e_E)*(\frac{(1+i)^n-(1+e_E)^n}{(1+i)^n*(i-e_E)})$

  $d_{Wartung} = (1+e_A)*(\frac{(1+i)^n-(1+e_A)^n}{(1+i)^n*(i-e_A)})$
  
- if only own capital or a one-off funding is used, then $i = i_{EK}$  
- if loan is used, then $i = i_{m}$  
 
$i_m = \frac{((i_{EK}*Eigenkapital)+(i_{FK}*Fremdkapital))}{Eigenkaptial+Fremdkaptial}$
- detailed discounting maintaince cost formula
  
$A_{Wartung_Wind} = 0.05 * A_0$  

$A_{Wartung_PV} = 0.025 * A_0$

- variable meanings

    | Variable    | Bedeutung            |
    |-------------|------------          |
    | $A_0$       | initial investment    |
    | $A_{Name}$    |  costs            |
    | $d_{Name}$ | discount interest |
    | $E_{Name}$ | yield |
    | $i_{EK}$ | own captial interest |
    | $i_{FK} $|  outside captial interes |
    | $i_{m}$ | mixed interest of own and outside capital |

## How To Use:
- configuring the variables in the main method
- if land is not leased, lease_price = 0
- ff  EK, FK is not used, set this also to 0
- run main.py
