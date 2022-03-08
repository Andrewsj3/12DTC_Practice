def validate_name(prompt):
    name = input(prompt)
    while not name.isalpha():
        print("Name cannot be blank, please enter again.")
        name = input(prompt)
    return name
