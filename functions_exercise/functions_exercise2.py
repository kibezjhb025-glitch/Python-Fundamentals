# Exercise 2: Functions with and without Parameters
# We will also put into practice what you did or learned on control structures
# Please mind your arguments!!!!
import sys

# 1. Write a function without a parameter called 'get_user_input'
    # This function must take user inputs 'Username, age and email'
    # validate the AGE using a loop and conditional statements
        # If the AGE is not an Integer print "Not an Integer, Enter a valid age!"
        # If the AGE is less than 17 print "You are young"
        # If the Age is more than 65 print "You are too old"  
    # Return all the inputs
def get_user_input(username = None, age= None, email =None ):
    if username is None:
        username = input("Enter your username: ")
    
    while True:
        age_str = input("Enter your age: ")
        if not str(age_str).isdigit():
            print("Not an Integer, Enter a valid age!")
            continue
    
        age = int(age_str)
        if age < 17:
            print("You are young")
        elif age > 65:
            print("You are too old")
        break

    email = input("Enter your email: ")
    return username, age, email




# 2. On the function below 'validate_username'
    # Validate the username that comes as a parameter
    # Use a loop to check all the characters on the username 
    # If the chars are not strings return False else return True
    # If the username is an empty string return False
    # Return the boolean

def validate_username(username):
    
    if username == "":
        return False
    for char in username:
        if not char.isalpha():
            return False
    return True

# 3. Pass the parameters to the function below 'display_user_info'
    # Underneath the User Information print the following:
        # 'Username : <username>'
        # 'Age      : <age>'
        # 'Email    : <email>
    # return 'Thanks!, Details captured.'

def display_user_info(username, age, email, output=sys.stdout):
   
    print(f"\nUser Information:\nUsername : {username}\nAge      : {age}\nEmail    : {email}", file=output)
    return "Thanks!, Details captured."

   

# 4. Call all the functions
    # If 'validate_username' function returns False
        # write a loop to and take new input for the username and take it to be evaluated 'validate_username'
    # if 'validate_username' returns True then you can display the user Info   
def main():
    username, age, email = get_user_input()

    while not validate_username(username):
        print("Invalid username. Only letters allowed and cannot be empty.")
        username = input("Enter a valid username: ")

    message = display_user_info(username, age, email)
    print(message)

if __name__ == "__main__":
    main()