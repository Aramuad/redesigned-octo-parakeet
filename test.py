
print("")
qts = float(input("Enter number of quarters: "))
dms = float(input("Enter number of dimes: "))
nkls = float(input("Enter numner of nickels: "))
pnis = float(input("Enter number of pennies: "))
name = ""
coins = {qts: .25, dms: .10, nkls: .05, pnis: .01}
total = ((qts * .25) + (dms * .10) + (nkls * .05) + (pnis * .01))

for coin in coins:    
    print("You entered " + str(coin) + name

    if coin.value == .25
        name = str("quarters.")
    if coin.value == .10
        name = str("dimes.")
    if coin.value == .05
        name = str("nickels.")
    if coin.value == .01
        name = str("pennies.")

print("")
print("Your total is " + str(total) + " Dollars")
