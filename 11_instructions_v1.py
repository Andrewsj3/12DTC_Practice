def show_instructions():
    print("*** Mega Movie Fundraiser Instructions ***")
    print("Instructions go here")


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
