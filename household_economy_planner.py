class HouseholdEconomyPlanner:
    def __init__(self, income, expenses):
        self.income = income
        self.expenses = expenses

    def calculate_balance(self):
        return self.income - self.expenses

    def is_in_surplus(self):
        return self.calculate_balance() > 0


# Get income and expense information from the user
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your monthly expenses: "))

planner = HouseholdEconomyPlanner(income, expenses)
balance = planner.calculate_balance()

print(f"Monthly budget balance: {balance}")
if planner.is_in_surplus():
    print("Your budget is in surplus.")
else:
    print("Your budget is in deficit.")
