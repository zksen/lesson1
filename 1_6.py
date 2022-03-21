name_us = input("What is your name? -> ")
rev = float(input("Enter your company's revenue -> "))
cost = float(input("Enter your company's costs -> "))
if rev > cost:
    print(f"Dear {name_us}, your company is profitable.Your profitability {rev / cost:.1f}!")
    staff = int(input("Enter the number of company employees. -> "))
    print(f"Profit per employee is {(rev - cost) / staff:.1f}")
else:
    print(f"Dear {name_us}, your company is not profitable!")
