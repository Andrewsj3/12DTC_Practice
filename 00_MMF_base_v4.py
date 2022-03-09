"""MMF_base_v4: Integrate get_age component into main program. It asks for the
user's age and checks that it is a valid integer between 12 and 110. If it is
under 12, it will say the user is too young, otherwise if it is above 110, the
user will be asked to re-enter.
Jack Andrews
9/03/22
"""


# Import statements

# Function definitions

# Check that the ticket name is not blank
def validate_name(prompt):
    name = input(prompt).title()  # Added title so names are capitalized
    while not name.isalpha():  # Checks that at least one letter is entered
        print("Name cannot be blank, please enter again.")  # Error message
        name = input(prompt)
    return name


# Code that gets the user's age and checks it is between 12 and 110
def get_age(prompt):
    from collections import namedtuple
    constants = namedtuple("consts", ["MIN_AGE", "MAX_AGE"])
    consts = constants(12, 110)  # Creating MIN_AGE and MAX_AGE constants
    while True:
        try:
            age = int(input(prompt))
            if age < consts.MIN_AGE:
                print("Sorry, you are too young for this movie.\n")
                return 0  # Will be used later in the program
            elif age > consts.MAX_AGE:
                return get_age(f"{age} is a very old age. Please re-enter "
                               "your age: ")
            else:
                return age
        except ValueError:
            print("Please enter an integer "
                  "(i.e. a whole number with no decimals)\n")


# Loop code for selling tickets
def loop():
    from collections import namedtuple
    constants = namedtuple("consts", "MAX_TICKETS")
    consts = constants(5)  # Creating the MAX_TICKETS constant
    count = 0
    print(f"You have {consts.MAX_TICKETS} seats left.")
    while True:
        name = validate_name("Please enter your name: ")
        if name == 'Xxx':  # Exit code for loop
            break
        else:
            age = get_age("Please enter your age: ")
            if age != 0:  # return value when user is under 12
                count += 1
        if count == consts.MAX_TICKETS:  # When 5 tickets have been sold
            break
        print(f"\nYou have{' ONLY' if count >= consts.MAX_TICKETS - 1 else ''}"
              f" {consts.MAX_TICKETS - count} "
              f"{'seats' if count < consts.MAX_TICKETS - 1 else 'seat'} left.")
        # Prints data on amount of seats available

    if count == consts.MAX_TICKETS:
        print("\nAll available tickets have been sold.")
    else:
        print(f"\nYou have sold {count} tickets.")
        print(f"There are still {consts.MAX_TICKETS - count} " 
              f"tickets available.")


# Main routine

# Initialize variables and data structures

# Ask user if they want instructions on how to use the program

# Start loop

# Get name (can't be blank)

# Get age (between 12 and 130)

# Calculate ticket price

# Ask for payment method (apply surcharge for credit)

# Calculate total sales and profit

# Output data to file (txt or csv)
