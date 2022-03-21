def get_choice(question, valid_choices):
    response = input(question).lower()
    for choices in valid_choices:
        if response in choices:
            return valid_choices.get(choices)

    else:
        print("Sorry, that is not a valid choice")
        return get_choice(question, valid_choices)


def apply_surcharge():
    from collections import namedtuple
    constants = namedtuple("const", "SURCHARGE_RATE")
    consts = constants(.05)
    valid_choices = {("credit card", "card", "credit", "cc", "cr", '1'):
                     "Credit Card",
                     ('2', "eft", "pos", "eftpos", 'e', "ep"): "Eftpos",
                     (
                     "ca", "cash", "money", "notes", "coins", 'c', '3'): "Cash"
                     }

    while True:
        surcharge = 0
        name = input("What is your name: ").title()
        if not name:
            continue
        if name == 'X':
            break
        subtotal = float(input("Subtotal: $"))
        payment_choice = get_choice("How would you like to pay? ",
                                    valid_choices)

        if payment_choice == "Credit Card":
            surcharge = (subtotal * consts.SURCHARGE_RATE)

        total_payable = subtotal + surcharge
        print(f"{name} | Subtotal: ${subtotal:.2f} | Surcharge:"
              f" ${surcharge:.2f} | The total payable is ${total_payable:.2f}")


if __name__ == '__main__':
    apply_surcharge()
