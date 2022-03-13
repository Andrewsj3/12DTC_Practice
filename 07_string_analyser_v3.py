def analyse_string():
    import re
    test_strings = [
        "Popcorn",
        "2 pc",
        "1.5OJ",
        "4OJ"]
    for item in test_strings:
        number_regex = r"^[1-9]"
        if re.match(number_regex, item):
            quantity = int(item[0])
            snack = item[1:]
        else:
            quantity = 1
            snack = item

        snack = snack.strip()

        print(f"{quantity = }")
        print(f"{snack = }")
        print(f"Length of snack: {len(snack)}")


if __name__ == '__main__':
    analyse_string()
