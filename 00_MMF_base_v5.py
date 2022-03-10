"""MMF_base_v5: Integrate calc_ticket_price component into the program. This
takes the user's age, and sees whether it is in the child range, the standard
range, or the senior age and then returns the price of the ticket and the
profit. Also changed the language in the print statements so it is easier to
understand.
Jack Andrews
10/03/22
"""


# Import statements

# Function definitions below

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


# Calculates price based on age
def calc_price(age):
    from collections import namedtuple
    constants = namedtuple("const", ["CHILD_AGE", "STANDARD_AGE",
                                     "TICKET_COST_PRICE"])
    # Creating constants for the age ranges and the ticket cost price
    consts = constants(range(12, 16), range(16, 65), 5)
    if age in consts.CHILD_AGE:
        ticket_price = 7.5
    elif age in consts.STANDARD_AGE:
        ticket_price = 10.5
    else:
        ticket_price = 6.5
    # Now returns the profit as well as the cost
    return ticket_price, ticket_price - consts.TICKET_COST_PRICE


# Loop code for selling tickets
def loop():
    from collections import namedtuple
    constants = namedtuple("consts", "MAX_TICKETS")
    consts = constants(5)  # Creating the MAX_TICKETS constant
    count = 0
    profit = 0
    print(f"There are {consts.MAX_TICKETS} tickets left.")
    while True:
        name = validate_name("Please enter ticket-holder's name: ")
        if name == 'Xxx':  # Exit code for loop
            break
        else:
            age = get_age(f"Please enter {name}'s age: ")
            if age != 0:  # return value when user is under 12
                count += 1
                ticket_price, ticket_profit = calc_price(age)
                print(f"For {name}, the price is ${ticket_price:.2f}")
                profit += ticket_profit

        if count == consts.MAX_TICKETS:  # When 5 tickets have been sold
            break
        print(f"\nThere"
              f"{' is ONLY' if count >= consts.MAX_TICKETS - 1 else ' are'} "
              f"{consts.MAX_TICKETS - count} "
              f"{'tickets' if count < consts.MAX_TICKETS - 1 else 'ticket'} "
              f"left.")
        # Prints data on amount of seats available

    if count == consts.MAX_TICKETS:
        print("\nAll available tickets have been sold.")
    else:
        print(f"\n{count} tickets have been sold.")
        if count == consts.MAX_TICKETS - 1:
            print("There is still 1 ticket available")
        else:
            print(f"There are still {consts.MAX_TICKETS - count} tickets "
                  "available")

    print(f"\nTicket profit is ${profit:.2f}")


# Structure of final program:

# Main routine starts

# Initialize variables and data structures

# Ask user if they want instructions on how to use the program

# Start loop

# Get name (can't be blank)

# Get age (between 12 and 110)

# Calculate ticket price

# Ask for payment method (apply surcharge for credit)

# Calculate total sales and profit

# Output data to file (txt or csv)
