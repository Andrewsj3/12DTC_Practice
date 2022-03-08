"""MMF_base_v3: Integrate basic version of the ticket loop into main program,
which continually asks the user for their name until either 5 tickets have been
sold or the user enters 'xxx' as the name.
Jack Andrews
8/03/22
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
