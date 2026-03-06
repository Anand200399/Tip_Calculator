# Greetiong for the the application

print("Welcome to the Tip Calculator!")

# Ask the user for total bill amount and convert the input into float(decimal number) 
bill = float(input("What was the total bill? $"))

# Ask the user what percenatge tip they want to give and convert into float
tip = float(input("How much percentage tip would you like to give? 10, 12, or 15? "))

# Ask how many people will split the bill and convert into integer
people = int(input("How many people to split the bill? "))

# Mathematic operation
# Calculate the tip amount based on the bill and tip percentage
total_tip = (bill / 100) * tip

# Add the tip to the original bill 
total_bill = bill + total_tip

# Divide the total bill by the number of people to get how much each person should pay
each_person_to_pay = total_bill / people

# Round the amount to 2 decimal places for the purpose of amount values
final_each_person_to_pay = round(each_person_to_pay, 2)

# Print the final amount each person should pay
print(f"Each person should pay: ${final_each_person_to_pay}")
