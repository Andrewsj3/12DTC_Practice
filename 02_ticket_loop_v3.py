def loop():
    from collections import namedtuple
    constants = namedtuple("consts", "MAX_TICKETS")
    consts = constants(5)
    count = 0
    print(f"You have {consts.MAX_TICKETS} seats left.")
    while True:
        name = input("Please enter your name: ").title()
        if name == 'Xxx':
            break
        else:
            count += 1
        if count == consts.MAX_TICKETS:
            break
        print(f"\nYou have{' ONLY' if count >= consts.MAX_TICKETS - 1 else ''}"
              f" {consts.MAX_TICKETS - count} "
              f"{'seats' if count < consts.MAX_TICKETS - 1 else 'seat'} left.")

    if count == consts.MAX_TICKETS:
        print("\nAll available tickets have been sold.")
    else:
        print(f"\nYou have sold {count} tickets.")
        print(f"There are still {consts.MAX_TICKETS - count} " 
              f"tickets available.")
