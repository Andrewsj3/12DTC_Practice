def main():
    import pandas
    names = ["Rangi", "Manaia", "Talia", "Arihi", "Fetu"]
    tickets = [7.5, 10.5, 10.5, 10.5, 6.5]
    popcorn = [0] * 5
    mms = [0] * 5
    pita_chips = [0] * 5
    water = [0] * 5
    orange_juice = [0] * 5
    movie_data_dict = {
        "Name": names,
        "Ticket": tickets,
        "Popcorn": popcorn,
        "M&Ms": mms,
        "Pita Chips": pita_chips,
        "Water": water,
        "Orange Juice": orange_juice
    }
    prices = {
        "Popcorn": 2.5,
        "M&Ms": 3,
        "Pita Chips": 4.5,
        "Water": 2,
        "Orange Juice": 3.25
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
    movie_frame["Sub Total"] = movie_frame["Ticket"]
    for heading in list(movie_frame)[1:-1]:
        movie_frame["Sub Total"] += movie_frame[heading] * prices.get(heading)
        # I don't know how it works, or why it works, but it does
    movie_frame = movie_frame.rename(columns={"Orange Juice": "OJ",
                                              "Pita Chips": "Chips"})
    print(movie_frame)


if __name__ == '__main__':
    main()
