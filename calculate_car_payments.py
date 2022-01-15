import sys, numpy_financial as npf

usage_string = "python3 calculate_car_payments.py [Principle] [Down payment] [Interest rate (APY)] [Term Length (Years)]" 
P = float(sys.argv[1]) # Principle amount
D = float(sys.argv[2]) # Down payment
I = float(sys.argv[3]) # Interest rate (APY)
T = float(sys.argv[4]) # Term length (Years)

car_payments = npf.pmt(rate = I/12, nper = T*12, pv = (D - P))
print("Monthly payments: $%4.2f" % car_payments)
