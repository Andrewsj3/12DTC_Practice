def validate_name(prompt, error_msg):
    name = input(prompt)
    while not name:
        print(error_msg)
        name = input(prompt)
    return name
