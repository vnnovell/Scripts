import sys
def calculate_tax(MSRP,TRADE_IN, TAX_RATE):
    NET_PRICE = MSRP - TRADE_IN
    TAX = TAX_RATE * NET_PRICE
    return TAX
usage_string = "python3 calculate_car_price_autopark.py [MSRP] <TRADE_IN>" 
try: 
    MSRP = float(sys.argv[1])
except ValueError: 
    print("Cannot convert first input argument to float")
    print(usage_string)
try: 
    TRADE_IN = float(sys.argv[2])
except ValueError:
    print("Cannot convert second input argument to float")
    print(usage_string)
except:
    TRADE_IN = 0
TAX_RATE_NC = 0.03
REG_FEE_AP = 77.50
ADMIN_FEE_AP = 698.00
TAX = calculate_tax(MSRP,TRADE_IN,TAX_RATE_NC)
TOTAL_COST = (MSRP - TRADE_IN) + TAX + REG_FEE_AP + ADMIN_FEE_AP
print("Total cost of vehicle is: %6.2f" % TOTAL_COST)

