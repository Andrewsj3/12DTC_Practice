"""MMF_base_v11: Final version: Includes instructions that can be shown at the
user's request.
Jack Andrews
22/03/22
"""

# Import statements
from collections import namedtuple  # For creating constants


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
    constants = namedtuple("const", "MAX_NUMBER_OF_SNACKS")
    consts = constants(4)  # Creating the max amount of snacks constant
    snacks = []
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


def get_choice(question, valid_choices):
    response = input(question).lower()
    for choices in valid_choices:  # Iterates through a dictionary containing
        # the possible choices (see valid_snacks and payment_methods) and
        # checks if input is in one of those choices
        if response in choices:
            return valid_choices.get(choices)

    else:
        print("Sorry, that is not a valid choice")
        return get_choice(question, valid_choices)


def summary(snacks_ordered):
    if snacks_ordered:
        print("\nThis is a summary of your order:")
        for qty, item in snacks_ordered:
            print(f"\t{item}, amount ordered: {qty}")
    else:
        print("No snacks were ordered")


# Takes a subtotal, checks if payment method is credit, and if so, appends
# surcharge, else, appends 0 to surcharge
def calc_surcharge(subtotal, payment_methods, surcharge: list):
    constants = namedtuple("const", "SURCHARGE_RATE")
    consts = constants(.05)
    payment_method = get_choice("How would you like to pay? ",
                                payment_methods)
    if payment_method == "Credit Card":
        surcharge.append(round(subtotal * consts.SURCHARGE_RATE, 2))
    else:
        surcharge.append(0)


def show_instructions():
    print("*** Mega Movie Fundraiser Instructions ***\n")
    print('*'*70)
    print("\n You will be shown how many tickets are available for sale\n"
          " and then asked for the first ticket-purchaser's name.\n"
          " You will then be asked to input their age. This is because:\n"
          " The minimum age for entry is 12; and there is a standard price\n"
          " for adults; but different prices for students and seniors.\n"
          " The program will then ask you for snack orders. You do this by\n"
          " entering the quantity of a snack if you want more than one, then\n"
          " the snack name. Enter 'x' to finish. Now the program moves on to\n"
          " payment. You will need to enter a valid payment method\n"
          " (credit, cash, or eftpos). This repeats until all seats have\n"
          " been sold or you choose to exit the program. On exit, a summary\n"
          " of sales and profits will be displayed. Full details are also\n"
          " exported to csv files. These will be located in the same\n"
          " directory as the program.\n")
    print('*'*70, '\n')


# Loop code for selling tickets and snacks (main part of the code)
def loop(movie_data_dict):
    constants = namedtuple("consts", ["MAX_TICKETS", "SURCHARGE_RATE",
                                      "SNACK_PROFIT_MARGIN"])
    consts = constants(150, .05, .2)  # Creating the various constants
    count = 0  # How many tickets have been sold
    profit = 0  # Ticket profit
    valid_snacks = {('popcorn', 'p', 'corn', 'pop', '1'): "Popcorn",
                    ('m&ms', 'mms', 'm', 'mn', '2'): "M&Ms",
                    ('pita chips', 'chips', 'pc', 'pita', 'c', '3'):
                    "Pita Chips",
                    ('w', 'water', '4'): "Water",
                    ("orange juice", "oj", "5"): "Orange Juice"}
    payment_methods = {("credit card", "card", "credit", "cc", "cr", '1'):
                       "Credit Card",
                       ('2', "eft", "pos", "eftpos", 'e', "ep"): "Eftpos",
                       ("ca", "cash", "money", "notes", "coins", 'c', '3'):
                       "Cash"}
    prices = {
        "Popcorn": 2.5,
        "M&Ms": 3,
        "Pita Chips": 4.5,
        "Water": 2,
        "Orange Juice": 3.25
    }
    print(f"There are {consts.MAX_TICKETS} tickets left.")

    while True:
        subtotal = 0
        name = validate_name("Please enter ticket-holder's name: ")
        if name == 'X':  # Exit code for loop
            break

        else:
            movie_data_dict.get("Name").append(name)
            age = get_age(f"Please enter {name}'s age: ")
            if age != 0:  # return value when user is under 12
                count += 1
                ticket_price, ticket_profit = calc_price(age)
                print(f"For {name}, the price is ${ticket_price:.2f}")

                profit += ticket_profit
                subtotal += ticket_price
                movie_data_dict.get("Ticket").append(ticket_price)

                order = get_snacks(
                    "What snack do you want - 'x' to stop ordering: ",
                    valid_snacks)
                price = 0
                if order:  # Is not blank
                    for qty, snack in order:
                        price += prices.get(snack) * qty
                        subtotal += prices.get(snack) * qty
                        movie_data_dict.get(snack)[count-1] = qty
                movie_data_dict.get("Snack Cost").append(price)
                movie_data_dict.get("Snack Profit").\
                    append(round(price * consts.SNACK_PROFIT_MARGIN, 2))
                # Updating the lists in movie_data_dict
                summary(order)
                calc_surcharge(subtotal, payment_methods,
                               movie_data_dict["Surcharge"])

                movie_data_dict.get("Subtotal").append(subtotal)
                movie_data_dict.\
                    get("Total").append(subtotal + movie_data_dict.
                                        get("Surcharge")[count-1])
                # My long-winded way of adding the subtotal and surcharge
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

    print(f"\nTotal profit is $"
          f"{profit+sum(movie_data_dict.get('Snack Profit')):.2f}")
    return profit, count


def main():
    import pandas as pd
    constants = namedtuple("consts", "MAX_TICKETS")
    consts = constants(150)
    all_names = []
    all_tickets = []
    surcharge = []
    snack_cost = []
    snack_profit = []
    popcorn = [0] * consts.MAX_TICKETS
    # Initialising lists at maximum possible length so zeros don't have to
    # be manually recorded (for snack lists only)
    mms = [0] * consts.MAX_TICKETS
    pita_chips = [0] * consts.MAX_TICKETS
    water = [0] * consts.MAX_TICKETS
    orange_juice = [0] * consts.MAX_TICKETS
    subtotal = []
    total = []
    movie_data_dict = {
        "Name": all_names,
        "Ticket": all_tickets,
        "Popcorn": popcorn,
        "M&Ms": mms,
        "Pita Chips": pita_chips,
        "Water": water,
        "Orange Juice": orange_juice,
        "Snack Cost": snack_cost,
        "Snack Profit": snack_profit,
        "Subtotal": subtotal,
        "Surcharge": surcharge,
        "Total": total
    }
    summary_headings = \
        [value for value in list(movie_data_dict)[2:7]]
    summary_headings.extend(["Snack Profit", "Ticket Profit", "Total Profit"])
    # Populating summary headings using the keys in movie_data_dict
    summary_data = []
    # print(summary_headings)
    summary_data_dict = {
        "Item": summary_headings,
        "Amount": summary_data
    }
    print("\tWelcome to Mega Movie!\n")
    if yes_no("Do you want to see the instructions? "):
        show_instructions()

    ticket_profit, iterations = loop(movie_data_dict)
    if not snack_cost:  # No one ordered snacks - unlikely but possible
        movie_data_dict["Snack Cost"] = [0]
        movie_data_dict["Snack Profit"] = [0]
    for key, item in movie_data_dict.items():
        movie_data_dict[key] = movie_data_dict.get(key)[:iterations]
    # Shortening lists to the same size so the dataframe works correctly

    movie_currencies = ["Ticket", "Snack Cost", "Subtotal", "Surcharge",
                        "Total"]
    for lst in movie_currencies:
        for idx, item in enumerate(movie_data_dict[lst]):
            # noinspection PyTypeChecker
            movie_data_dict[lst][idx] = f"${item}"
            # Formatting currency amounts, also ignore above comment - it is
            # meant for the type checker

    pd.set_option("display.max_columns", None)  # Shows all columns
    movie_frame = pd.DataFrame(movie_data_dict)
    movie_frame = movie_frame.set_index("Name")
    movie_frame = movie_frame.rename(columns={"Pita Chips": "Chips",
                                              "Orange Juice": "OJ"})

    summary_data.extend(sum(item) for item in list(movie_data_dict.values())
                        [2:7])
    # Populating summary_data with the sum of the snack_lists
    total_profit = ticket_profit + (snack_profit :=
                                    sum(movie_data_dict["Snack Profit"]))
    summary_currencies = [snack_profit, ticket_profit, total_profit]
    for amount in summary_currencies:
        amount = f"${amount:.2f}"
        summary_data.append(amount)
    # Ticket profit is total profit - snack profit
    summary_frame = pd.DataFrame(summary_data_dict)
    summary_frame = summary_frame.set_index("Item")

    movie_frame.to_csv("ticket_details.csv")
    summary_frame.to_csv("snack_summary.csv")

    print("\n*** Ticket/Snack Information ***\n")
    print("Note: For full details see excel file called snack_summary.csv and "
          "ticket_details.csv\n")
    print(movie_frame[["Ticket", "Snack Cost", "Subtotal",
                       "Surcharge", "Total"]])
    print("\n*** Snack/Profit Summary ***\n")
    print(summary_frame)


if __name__ == '__main__':
    main()
