
# Class:	CSE 1321L
# Section: 1         
# Term: Spring/2019  
# Instructor: Amier Cher 
# Name: Samuel Ballard
# Lab#: 3


# SumValue
 
# Psuedocode

# TAKE THREE NUMBERS AS INPUT FROM A USER
# PRINT EACH INPUT ON ITS OWN LINE
# PRINT AVERAGE OF INPUTS ON ITS OWN LINE

# DEFINE VARIABLES TO HOLD USER INPUT
# STRINGIFY USER INPUT TO ENABLE PRINTING
# PRINT USER INPUT
# ADD USER INPUT AND DIVIDE BY THREE FOR AVERAGE
# STRIGIFY AND PRINT AVERAGE

# IT TOOK ME A LONG TIME TO WRITE ALL THIS BECAUSE I ONLY KNOW SOME RUBY
# SYNTAX SEEMS SIMILAR SO FAR

# ADDED PRETTY EMPTY STRING PRINT SPACES CAUSE I DONT KNOW HOW TO DO FLAMES YET

# PROGRAM RUNS, STILL NEED TO WRITE TESTS

print("")
x = input("Let's average three numbers, select an integer and press enter: ")
print("")
y = input("Select 2 more integers: ")
print("")
z = input("Enter the final integer and press enter: ")
print("")

print("X = " + str(x))
print("Y = " + str(y))
print("Z = " + str(z))
print("Average = " + str((x+y+z)/3))

# END

# SimpleMath 

# Psuedocode

# TAKE TWO INTEGERS FROM USER
# ADD, SUBTRACT, AND MULTIPLY THE TWO INTEGERS
# PRINT INTEGERS AND SOLUTIONS FOR EACH EVALUATION ON OWN LINE

# DEFINE VARIABLES TO STORE USER INPUT
# DEFINE VARIABLES FOR EVALUATIONS
# PRINT USER INPUT AND SOLUTIONS ON OWN LINE

# EVERYTHING IS BROKEN, MY LIFE IS A LIE
# NEED TO CONVERT INPUT TO FLOAT TO PERFORM OPERATIONS
# NEED TO STRINGIFY SOLUTIONS TO ENABLE CONCATINATION

# ADD FLOAT FUNCTION TO INSIDE OF INPUT FUNCTION
# ADD STRING FUNTION TO ENABLE PRINTING

# BREAKS BECAUSE FLOAT FUNCTION SHOULD WRAP INPUT FUNCTION

print("")
r = float(input("Enter first number: "))
t = float(input("Enter second number: "))
add = r + t
sub = r - t
pro = r * t

print("R = " + str(r))
print("T = " + str(t))
print("R + T = " + str(add)
print("R - T = " + str(sub)
print("R * T = " + str(pro)

# END

# Coins 

# Psuedocode

# PROMPT THE USER TO ENTER HOW MUCH OF EACH US COIN THE JAR HOLDS
# STORE USER INPUT
# ADD AND PRINT VALUE OF SUM OF ALL COINS IN JAR IN TERMS OF DOLLARS AND CENTS

# DEFINE ONE VARIABLE FOR EACH COIN TO HOLD USER INPUT
# MULTIPLY EACH COIN VARIABLE BY ITS CORESPONDNG DECIMAL VALUE AND SUM RESULTS
# PRINT THE AMOUNT OF EACH COIN ENTERED ON SEPPERATE LINES
# PRINT TOTAL ON ITS OWN LINE

# DOES NOT HANDLE INTEGERS AS EXPECTED
# NEED TO MASSAGE DATA

# CONVERT USER INPUT TO FLOAT TO ENABLE OPERATIONS TO BE PERFORMED
# STRINGIFY RESULTS OF OPERATIONS TO ALLOW PRINTING
# NEVER FIGURED OUT HOW TO DISPLAY WHOLE DOLLARS AND CENTS SEPERATELY 

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

# END

