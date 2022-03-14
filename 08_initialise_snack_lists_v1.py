def initialise_snack_lists():
    names = ["Rangi", "Manaia", "Talia", "Arihi", "Fetu"]
    popcorn = [0] * 5
    mms = [0] * 5
    pita_chips = [0] * 5
    water = [0] * 5
    orange_juice = [0] * 5
    snack_lists = [popcorn, mms, pita_chips, water, orange_juice]
    snack_menu_dict = {
        "Popcorn": popcorn,
        "Water": water,
        "Pita Chips": pita_chips,
        "M&Ms": mms,
        "Orange Juice": orange_juice
    }
    test_data = [
        [[2, "Popcorn"], [1, "Pita Chips"], [1, "Orange Juice"]],
        [[]],
        [[1, "Water"]],
        [[1, "Popcorn"], [1, "Orange Juice"]],
        [[1, "M&Ms"], [1, "Pita Chips"], [3, "Orange Juice"]]
    ]
    for count, item in enumerate(test_data):
        try:
            for qty, snack in item:
                snack_menu_dict.get(snack)[count] = qty
        except ValueError:  # No snacks ordered
            continue

    print(f"{popcorn = }")
    print(f"{mms = }")
    print(f"{pita_chips = }")
    print(f"{water = }")
    print(f"{orange_juice = }")


if __name__ == '__main__':
    initialise_snack_lists()
