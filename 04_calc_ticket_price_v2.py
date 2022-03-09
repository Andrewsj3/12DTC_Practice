def calc_price(age):
    from collections import namedtuple
    constants = namedtuple("const", ["CHILD_AGE", "STANDARD_AGE"])
    consts = constants(range(12, 16), range(16, 65))
    if age in consts.CHILD_AGE:
        ticket_price = 7.5
    elif age in consts.STANDARD_AGE:
        ticket_price = 10.5
    else:
        ticket_price = 6.5
    return ticket_price


if __name__ == '__main__':
    test_cases = [["Rangi", 15], ["Manaia", 16], ["Talia", 64], ["Arihi", 65]]
    for name, age in test_cases:
        print(f"For {name}, the price is ${calc_price(age):.2f}")
