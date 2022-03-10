def yes_no(question):
    response = input(question).lower()
    while True:
        if response[0] == 'y':
            return True
        elif response[0] == 'n':
            return False
        else:
            print("Invalid response, please enter Y or N")
            response = input(question).lower()


if __name__ == '__main__':
    while True:
        if yes_no("Do you want snacks? "):
            print("Valid answer, you do want snacks")
        else:
            print("Valid answer, you don't want snacks")
