def get_snacks():
    valid_snacks = {('popcorn', 'p', 'corn', '1'): "Popcorn",
                    ('m&ms', 'mms', 'm', '2'): "M&Ms",
                    ('pita chips', 'chips', 'pc', 'pita', 'c', '3'):
                        "Pita chips",
                    ('w', 'water', '4'): "Water"}

    snack_choice = input("Snack: ").lower()
    for snack in valid_snacks:
        if snack_choice in snack:
            return valid_snacks.get(snack)

    else:
        print("Sorry, that is not a valid choice")
        return get_snacks()


# if __name__ == '__main__':
#     for test in range(6):
#         print(f"You want: {get_snacks()}")
