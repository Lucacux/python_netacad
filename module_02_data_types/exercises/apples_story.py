# Create the variables: john, mary, and adam;
# Assign values to the variables. The value should be the number of apples each person had;
# Once the numbers are stored in the variables, print the variables on one line, and separate each of them with a comma;
# Then create a new variable called total_apples and set it equal to the sum of the three previous variables;
# Print the value stored in total_apples to the console;
# Experiment with your code: create new variables, assign different values to them, and perform various arithmetic operations with them (e.g., +, -, *, /, //, etc.). 
# Try combining a string with an integer in the same line, for example, "Total number of apples:" and total_apples.
# Vars. are defined.
john_apples = 3
mary_apples = 5
adam_apples= 6
# Total sum of vars.
total_apples = john_apples + mary_apples + adam_apples
# Vars output.
print("Jonh has", john_apples,"apples")
print("Mary has", mary_apples, "apples")
print("Adam has", adam_apples, "apples")
print("Total apples:", total_apples)
# Playing with conditionals in python.
if john_apples < mary_apples:
    print("John has fewer apples than Mary.")

if mary_apples > john_apples:
    print("Mary has more apples than John.")

if mary_apples < adam_apples:
    print("Mary has fewer apples than Adam.")

if adam_apples > mary_apples:
    print("Adam has more apples than Mary.")
    
if adam_apples > john_apples and adam_apples > mary_apples:
    print("Adam has the highest number of apples: ", adam_apples)
