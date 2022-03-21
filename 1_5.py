name_us = input("What is your name? -> ")
rev = float(input("Enter your company's revenue -> "))
cost = float(input("Enter your company's costs -> "))
if rev > cost:
    print(f"Dear {name_us}, your company is profitable.Your profit {rev - cost:.1f}!")
else:
    print(f"Dear {name_us}, your company is not profitable. Your losses {cost - rev:.1f}!")
