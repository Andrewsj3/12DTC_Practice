def show_instructions():
    print("*** Mega Movie Fundraiser Instructions ***\n")
    print('*'*70)
    print("\n You will be shown how many tickets are available for sale\n"
          " and then asked for the first ticket-purchaser's name.\n"
          " You will then be asked to input their age. This is because:\n"
          " The minimum age for entry is 12; and there is a standard price\n"
          " for adults; but different prices for students and seniors.\n"
          " The program will then ask you for snack orders. You do this by\n"
          " entering the quantity of a snack if you want more than one, then\n"
          " the snack name. Enter 'x' to finish. Now the program moves on to\n"
          " payment. You will need to enter a valid payment method\n"
          " (credit, cash, or eftpos). This repeats until all seats have\n"
          " been sold or you choose to exit the program. On exit, a summary\n"
          " of sales and profits will be displayed. Full details are also\n"
          " exported to csv files. These will be located in the same\n"
          " directory as the program.\n")
    print('*'*70)


def yes_no():
    response = input("Do you want to read the instructions? ").lower()
    while True:
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print("Invalid response, please enter Y or N")
            response = input("Do you want to read the instructions? ").lower()


if __name__ == '__main__':
    if yes_no():
        show_instructions()
        print("Launching program...")
    else:
        print("Instructions skipped, launching program...")
