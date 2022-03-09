from collections import namedtuple


def calc_price(age):
    constants = namedtuple("const", ["CHILD_AGE", "STANDARD_AGE"])
    consts = constants(range(12, 16), range(16, 65))
    if age in consts.CHILD_AGE:
        ticket_price = 7.5
    elif age in consts.STANDARD_AGE:
        ticket_price = 10.5
    else:
        ticket_price = 6.5
    return ticket_price


# if __name__ == '__main__':
#     TICKET_COST_PRICE = 5
#     profit = 0
#     test_cases = [["Rangi", 15], ["Manaia", 16], ["Talia", 64], ["Arihi", 65]
#     ]
#     for name, age in test_cases:
#         price = calc_price(age)
#         print(f"For {name}, the price is ${price:.2f}")
#         profit += price - TICKET_COST_PRICE
#     print(f"\nProfit is ${profit:.2f}")
