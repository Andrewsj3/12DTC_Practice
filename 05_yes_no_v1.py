def yes_no():
    response = input("Do you want snacks? ").lower()
    while True:
        if response in ['y', 'yes']:
            print("Valid answer, you do want snacks")
            break
        elif response in ['n', 'no']:
            print("Valid answer, you don't want snacks")
            break
        else:
            print("Invalid response, please enter Y or N")
            response = input("Do you want snacks? ").lower()


if __name__ == '__main__':
    yes_no()
