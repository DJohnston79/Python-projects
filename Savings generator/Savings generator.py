# --- Display a greeting ---
name = input("Hello. Please type your name: ")
print(f" Hello, {name.title()}.")
print("Let's get started , shall we?")

# --- Calculate the monthly savings ---

monthly_salary = int(input(f"{name.title()}.Please input you monthly salary after taxes: "))
expenditures = int(input("Please type the total amount of expneditures you have per month: "))

savings = monthly_salary - expenditures

print(f"{name.title()}. You have {savings} left over per month that you can put towards your savings.")