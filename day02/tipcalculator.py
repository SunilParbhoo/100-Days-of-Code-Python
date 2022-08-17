print("Welcome to the tip calculator.")
total = float(input("What was the total bill? $"))
split = int(input("How many people to split the bill between? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?  "))
payment = total * (1 + tip / 100) / split
# payment = round(payment, 2)
print(f"Each person should pay ${payment:.2f}")
