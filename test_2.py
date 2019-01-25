
print("")
qts = float(input("Enter number of quarters: "))
dms = float(input("Enter number of dimes: "))
nkls = float(input("Enter numner of nickels: "))
pnis = float(input("Enter number of pennies: "))
total = ((qts * .25) + (dms * .10) + (nkls * .05) + (pnis * .01))

print("You entered " + str(qts) + " quarters.")
print("You entered " + str(dms) + " dimes.")
print("You entered " + str(nkls) + " nickels.")
print("You entered " + str(pnis) + " pennies.")

print("")
print("Your total is " + str(total) + " Dollars")

