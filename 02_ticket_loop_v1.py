def loop():
    from collections import namedtuple
    constants = namedtuple("consts", "MAX_TICKETS")
    consts = constants(5)
    count = 0
    name = ''
    while name != "Xxx" and count != consts.MAX_TICKETS:
        name = input("Please enter your name: ").title()
        count += 1
