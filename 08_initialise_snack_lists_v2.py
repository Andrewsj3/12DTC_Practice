def main():
    import pandas
    names = ["Rangi", "Manaia", "Talia", "Arihi", "Fetu"]
    popcorn = [0] * 5
    mms = [0] * 5
    pita_chips = [0] * 5
    water = [0] * 5
    orange_juice = [0] * 5
    snack_lists = [popcorn, mms, pita_chips, water, orange_juice]
    movie_data_dict = {
        "Name": names,
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
                movie_data_dict.get(snack)[count] = qty
        except ValueError:  # No snacks ordered
            continue

    movie_frame = pandas.DataFrame(movie_data_dict)
    movie_frame = movie_frame.set_index("Name")
    print(movie_frame)


if __name__ == '__main__':
    main()
