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
    snacks = []
    want_snacks = yes_no("Do you want snacks? ")
    if want_snacks:
        while True:
            choice = input(question).lower()
            if choice != 'x':
                for snack in valid_choices:
                    if choice in snack:
                        snacks.append(valid_choices.get(snack))
                        break
                else:
                    print("Sorry, that is not a valid choice")
            else:
                break

    return snacks


# if __name__ == '__main__':
#     ask_for_snack = "What snack do you want - 'x' to stop ordering: "
#     valid_snacks = {('popcorn', 'p', 'corn', '1'): "Popcorn",
#                     ('m&ms', 'mms', 'm', '2'): "M&Ms",
#                     ('pita chips', 'chips', 'pc', 'pita', 'c', '3'):
#                         "Pita Chips",
#                     ('w', 'water', '4'): "Water"}
#
#     order = get_snacks(ask_for_snack, valid_snacks)
#     if order:
#         print("\nThis is a summary of your order:")
#         for item in order:
#             print(f"\t{item}")
#     else:
#         print("No snacks were ordered")


