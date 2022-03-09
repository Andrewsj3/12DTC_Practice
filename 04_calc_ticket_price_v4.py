def calc_price(age):
    from collections import namedtuple
    constants = namedtuple("const", ["CHILD_AGE", "STANDARD_AGE",
                                     "TICKET_COST_PRICE"])
    consts = constants(range(12, 16), range(16, 65), 5)
    if age in consts.CHILD_AGE:
        ticket_price = 7.5
    elif age in consts.STANDARD_AGE:
        ticket_price = 10.5
    else:
        ticket_price = 6.5
    return ticket_price, ticket_price - consts.TICKET_COST_PRICE
