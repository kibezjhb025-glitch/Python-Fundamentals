""" 
Exercise: Conditional Statements
In this exercise, you will use conditional statements to categorise people based on their ages.
"""

# 1. Ask the user for their age as input and convert it to an integer.
# Convert the user_age_str to an integer
# 2. Use conditional statements to categorise the user into one of the following categories:
# - If age is less than 18, print "You are a minor."
# - If age is between 18 and 65 (inclusive), print "You are an adult."
# - If age is 66 or higher, print "You are a senior citizen."
user_age = int(input("How old are you? "))

if user_age < 18:
    print("You are a minor")
elif 18  <= user_age <= 65 :
    print("You are an adult")
else:
    print("You are a senior citizen")

"""
Exercise: Loops
In this exercise, you will use a loop to print numbers up to a user-defined limit.
"""

# 1. Ask the user to enter a number as the limit and convert it to an integer.
# Convert the limit_str to an integer
# 2. Use a  for loop to iterate from 1 to the user-defined limit (inclusive) and print each number.
# Use a while loop to iterate from 1 to the user-defined limit (inclusive) and print each number.
# Initialise a variable to start the loop

limit = int(input("Enter a number as the limit: "))
# limit_str = input("Enter number limit")
# limit= int(limit_str)

print("FOR LOOP")
for i in range(1, limit +1 ):
    print(i)

print("WHILE LOOP")
i = 1
while i <= limit:
    print(i)
    i += 1
"""
Exercise: Loop Control Statements
In this exercise, you will use a loop and loop control statements to print odd numbers.
"""

# 1. Ask the user to enter a number as the limit and convert it to an integer.
# Convert the limit_str to an integer
# 2. Use a for loop to iterate from 1 to the user-defined limit (inclusive).
# 3. Inside the loop, use a loop control statement to skip even numbers and print odd numbers.

num_limit_str = input("Enter a number as the limit")
num_limit = int(num_limit_str)

for i in range(1,num_limit + 1):
    if i % 2 == 0:
        continue
    print(i)


"""
Exercise: Nested Loops
In this exercise, you will use nested loops to generate a multiplication table.

eg output:
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
...
10 x 1 = 10
10 x 2 = 20
10 x 3 = 30
"""

# 1. Ask the user for a number as the multiplier and convert it to an integer.
# Convert the multiplier_str to an integer
# 2. Use nested loops to generate a multiplication table.
# The outer loop iterates from 10 to 1.
# The inner loop iterates from the user-defined multiplier to 1.
# Fill in the code to complete the nested loops:

