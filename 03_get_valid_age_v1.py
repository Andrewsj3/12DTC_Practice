def get_age(prompt, low_age, high_age):
    while True:
        try:
            age = int(input(prompt))
            if age in range(low_age, high_age+1):
                return age
            else:
                print(f"Please enter an integer that is between {low_age} "
                      f"and {high_age}")
        except ValueError:
            print("Please enter an integer "
                  "(i.e. a whole number with no decimals)")


if __name__ == '__main__':
    get_age("Please enter your age: ", 12, 110)
