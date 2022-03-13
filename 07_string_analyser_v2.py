def analyse_string():
    test_strings = [
        "Popcorn",
        "2 pc",
        "1.5OJ",
        "4OJ",
        "12Chips"]
    for item in test_strings:
        if item[0].isdigit():
            if item[1].isdigit():
                quantity = int(item[0]+item[1])
                snack = item[2:]
            else:
                quantity = int(item[0])
                snack = item[1:]
        else:
            quantity = 1
            snack = item

        print(f"{quantity = }")
        print(f"{snack = }")


if __name__ == '__main__':
    analyse_string()
