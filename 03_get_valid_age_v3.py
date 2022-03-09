def get_age(prompt):
    from collections import namedtuple
    constants = namedtuple("consts", ["MIN_AGE", "MAX_AGE"])
    consts = constants(12, 110)
    while True:
        try:
            age = int(input(prompt))
            if age < consts.MIN_AGE:
                print("Sorry, you are too young for this movie.\n")
                return 0
            elif age > consts.MAX_AGE:
                print("Please enter an integer between 12 and 110.\n")
            else:
                return age
        except ValueError:
            print("Please enter an integer "
                  "(i.e. a whole number with no decimals)\n")


if __name__ == '__main__':
    get_age("Please enter your age: ")
