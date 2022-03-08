"""MMF_base_v2: Integrate the validate_name component into the main program,
which asks the user for their name and checks that it is not blank.
Jack Andrews
8/3/22
"""


# Import statements

# Function definitions

# Check that the ticket name is not blank
def validate_name(prompt):
    name = input(prompt)
    while not name.isalpha():  # Checks that at least one letter is entered
        print("Name cannot be blank, please enter again.")  # Error message
        name = input(prompt)
    return name


# Main routine

# Initialize variables and data structures

# Ask user if they want instructions on how to use the program

# Start loop

# Get name (can't be blank)
username = validate_name("Please enter your name: ")

# Get age (between 12 and 130)

# Calculate ticket price

# Ask for payment method (apply surcharge for credit)

# Calculate total sales and profit

# Output data to file (txt or csv)
