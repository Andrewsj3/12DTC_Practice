def analyse_string(string, regex):
    import re
    if len(string) == 1:
        return 1, string
    elif re.match(regex, string):
        qty = int(string[0])
        snack = string[1:]
    else:
        qty = 1
        snack = string

    snack = snack.strip()
    return qty, snack


def yes_no(question):
    response = input(question).lower()
    while True:
        if response[0] == 'y':
            return True
        elif response[0] == 'n':
            return False
        else:
            print("Invalid response, please enter Y or N")
            response = input(question).lower()


def get_snacks(question, valid_choices):
    from collections import namedtuple
    constants = namedtuple("const", "MAX_NUMBER_OF_SNACKS")
    consts = constants(4)
    snacks = []
    want_snacks = yes_no("Do you want snacks? ")
    if want_snacks:
        while True:
            choice = input(question).lower()
            if choice != 'x':
                qty, chosen_snack = analyse_string(choice, r"^[1-9]")
                if qty > consts.MAX_NUMBER_OF_SNACKS:
                    print("Sorry, the maximum number you can order is 4.")
                    continue
                for snack in valid_choices:
                    if chosen_snack in snack:
                        snacks.append((qty, valid_choices.get(snack)))
                        break
                else:
                    print("Sorry, that is not a valid choice")
            else:
                break

    return snacks


if __name__ == '__main__':
    ask_for_snack = "What snack do you want - 'x' to stop ordering: "
    valid_snacks = {('popcorn', 'p', 'corn', '1'): "Popcorn",
                    ('m&ms', 'mms', 'm', '2'): "M&Ms",
                    ('pita chips', 'chips', 'pc', 'pita', 'c', '3'):
                        "Pita Chips",
                    ('w', 'water', '4'): "Water",
                    ("orange juice", "oj", "5"): "Orange Juice"}

    order = get_snacks(ask_for_snack, valid_snacks)
    if order:
        print("\nThis is a summary of your order:")
        for amount, item in order:
            print(f"\t{item}, amount ordered: {amount}")
    else:
        print("No snacks were ordered")
