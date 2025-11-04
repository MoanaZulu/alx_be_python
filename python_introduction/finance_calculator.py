
print("Welcome to the Finance Calculator!")
print("Choose either 'simple' or 'compound' interest to proceed.")

interest_type = input("Enter the type of interest (simple/compound): ").lower()

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (as %): "))
time = int(input("Enter the number of years: "))

if interest_type == "simple":
    total = principal * (1 + (rate / 100) * time)
    print(f"After {time} years, your investment will be worth R{total:.2f} with simple interest.")
elif interest_type == "compound":
    total = principal * ((1 + (rate / 100)) ** time)
    print(f"After {time} years, your investment will be worth R{total:.2f} with compound interest.")
else:
    print("Invalid interest type selected. Please choose 'simple' or 'compound'.")
