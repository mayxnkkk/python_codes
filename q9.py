

principle = float(input("enter the principle amount:"))
rate = float(input("enter the annual interest rate :"))
time = float (input("enter the time (in year) :"))

simple_interest= (principle * rate * time) /100 

print(f"the simple interest is :{simple_interest:.2f}")