
print("Welcome To The Tip Calculator.")
total_bill = float(input("What was the total bill?  "))
tip_amount = int(input("What percentage tip would you like to give? 10, 12, or 15?  "))
people = int(input("How many people to split the bill:  "))

total_with_tip = (tip_amount/100 * total_bill) + total_bill
split_bill = total_with_tip/people

print("Each person will have to pay " + str(round(split_bill, 2)))