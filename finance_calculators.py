"""
Finance calculator to compute investment interest or bond repayments
based on user input.
"""

import math

print("Welcome to the Finance Calculator")
print("Please select either 'Investment' or 'Bond' from the menu below:")
print("Investment - calculate the interest you'll earn on your investment")
print("Bond - calculate the monthly repayment on a home loan")

# Take the user's input and convert to lowercase
user_choice = input("Enter your choice: ").lower()

# Check if the user input is valid
if user_choice not in ['investment', 'bond']:
    print("Invalid choice. Please select either 'Investment' or 'Bond'.")
elif user_choice == 'investment':
    principal = float(input("Enter the amount you want to invest: "))
    rate = float(input("Enter the interest rate (as a percentage, e.g., 8): ")) / 100
    time = float(input("Enter the number of years you want to invest for: "))

    interest_type = input("Do you want 'simple' or 'compound' interest? ").lower()
    if interest_type not in ['simple', 'compound']:
        print("Invalid choice. Please select either 'simple' or 'compound'.")
    else:
        if interest_type == 'simple':
            total_amount = principal * (1 + rate * time)
        else:  # compound interest
            total_amount = principal * math.pow((1 + rate), time)

        print(f"The total amount after {time} years will be: R{total_amount:.2f}")

elif user_choice == 'bond':
    present_value = float(input("Enter the present value of the house: "))
    annual_rate = float(input("Enter the interest rate (as a percentage, e.g., 7): "))
    monthly_rate = (annual_rate / 100) / 12
    months = float(input("Enter the number of months to pay off the bond: "))

    monthly_payment = (monthly_rate * present_value) / \
                      (1 - (1 + monthly_rate) ** (-months))
    print(f"The monthly payment will be: R{monthly_payment:.2f}")
