def get_snacks(question, valid_choices):
    response = input(question).lower()
    for snack in valid_choices:
        if response in snack:
            return valid_choices.get(snack)

    else:
        print("Sorry, that is not a valid choice")
        return get_snacks(question, valid_choices)


if __name__ == '__main__':
    ask_for_snack = "What snack do you want: "
    valid_snacks = {('popcorn', 'p', 'corn', '1'): "Popcorn",
                    ('m&ms', 'mms', 'm', '2'): "M&Ms",
                    ('pita chips', 'chips', 'pc', 'pita', 'c', '3'):
                        "Pita chips",
                    ('w', 'water', '4'): "Water"}
    for test in range(6):
        print(f"You have chosen {get_snacks(ask_for_snack, valid_snacks)}")
