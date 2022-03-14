"""MMF_base_v6: Integrate snack ordering into the program. The latest version
now allows user to order up to 4 of one snack at a time with the help of the
string analyser. Additionally,
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


# Takes the user's snack choice and splits it into a quantity, if given, and
# a snack choice
def analyse_string(string, regex):
    import re
    if len(string) == 1:  # For cases where the snack's reference number is
        # the only input
        return 1, string
    elif re.match(regex, string):  # Regex could be hard coded, but adding it
        # as a parameter allows flexibility if we want to change/improve it
        qty = int(string[0])
        snack = string[1:]
    else:
        qty = 1
        snack = string

    snack = snack.strip()  # Removes unnecessary whitespace
    return qty, snack


# Asks user yes or no question and returns True or False depending on response
def yes_no(question):
    response = input(question).lower()
    while True:
        if response[0] == 'y':  # Only looks at first letter of input
            return True
        elif response[0] == 'n':
            return False
        else:
            print("Invalid response, please enter Y or N")
            response = input(question).lower()


# Main component of snack ordering which uses the yes_no and analyse_string
# functions defined above
def get_snacks(question, valid_choices):
    from collections import namedtuple
    constants = namedtuple("const", "MAX_NUMBER_OF_SNACKS")
    consts = constants(4)  # Creating the max amount of snacks constant
    snacks = []
    want_snacks = yes_no("Do you want snacks? ")
    if want_snacks:
        while True:
            choice = input(question).lower()
            if choice != 'x':
                qty, chosen_snack = analyse_string(choice, r"^[1-9]")
                # Using analyse_string to split the input
                if qty > consts.MAX_NUMBER_OF_SNACKS:
                    print("Sorry, the maximum number you can order is 4.")
                    continue
                for snack in valid_choices:
                    if chosen_snack in snack:
                        snacks.append((qty, valid_choices.get(snack)))
                        # Keeps track of data for the summary
                        break
                else:
                    print("Sorry, that is not a valid choice")
            else:
                break

    return snacks


def summary(snacks_ordered):
    if snacks_ordered:
        print("\nThis is a summary of your order:")
        for qty, item in snacks_ordered:
            print(f"\t{item}, amount ordered: {qty}")
    else:
        print("No snacks were ordered")


# Loop code for selling tickets
def loop(names_list: list, tickets_list: list):
    from collections import namedtuple
    constants = namedtuple("consts", "MAX_TICKETS")
    consts = constants(5)  # Creating the MAX_TICKETS constant
    count = 0
    profit = 0
    valid_snacks = {('popcorn', 'p', 'corn', '1'): "Popcorn",
                    ('m&ms', 'mms', 'm', '2'): "M&Ms",
                    ('pita chips', 'chips', 'pc', 'pita', 'c', '3'):
                        "Pita Chips",
                    ('w', 'water', '4'): "Water",
                    ("orange juice", "oj", "5"): "Orange Juice"}
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
                names_list.append(name)
                tickets_list.append(ticket_price)
                order = get_snacks(
                    "What snack do you want - 'x' to stop ordering: ",
                    valid_snacks)
                summary(order)
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


def main():
    import pandas as pd
    all_names = []
    all_tickets = []
    movie_data_dict = {
        "Name": all_names,
        "Ticket": all_tickets
    }
    loop(all_names, all_tickets)
    movie_frame = pd.DataFrame(movie_data_dict)
    print(movie_frame)


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
if __name__ == '__main__':
    main()
