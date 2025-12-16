print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
step1=tip+bill
step2=step1/people
bill=round(step2,2)
print("Each should pay : $")
