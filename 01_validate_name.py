def validate_name():
    name = input("Please enter your name: ")
    while not name:
        print("Name cannot be blank, please enter again.")
        name = input("Please enter your name: ")
    return name
