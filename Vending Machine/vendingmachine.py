# setting items in the dictionary

items = {
    'Alcoholic Drinks': {
        1: {'item': 'Corona', 'price': 4.00},
        2: {'item': 'Budlight', 'price': 4.25},
        3: {'item': 'Vodka', 'price': 9.00},
        4: {'item': 'Soju', 'price': 6.00},
        5: {'item': 'Gin', 'price': 8.00}
    },
    'Chips': {
        5: {'item': 'Lays', 'price': 1.25},
        6: {'item': 'Pringles', 'price': 1.25},
        7: {'item': 'Doritos', 'price':1.25 }
    },
    'Chasers': {
        8: {'item': 'Berry Blast', 'price': 4.00},
        9: {'item': 'Pepsi', 'price': 5.00},
    },
    'Beverages': {
        10: {'item': 'Water', 'price': 1.00},
        11: {'item': 'Sparkling Water', 'price': 6.00},
        12: {'item': 'Orange Juice', 'price': 2.00},
        13: {'item': 'Coffee', 'price': 3.00},
    },
}

# Ask for user's age
while True:
    try:
        age = int(input("This establishment only serves those who are of age, please enter your age: "))
        break
    except ValueError:
        print("Invalid, please re-enter.")

if age >= 18:
    print("\nWelcome Customer!!")
    print("Here are the wide variety of items available:")

    for category, category_items in items.items():
        print(f"\n{category.capitalize()}:")
        for item_number, item_details in category_items.items():
            print(f"Item {item_number}: {item_details['item'].capitalize()} - Price: {item_details['price']} AED")

    # user money
    while True:
        try:
            money = float(input("\nPlease enter amount of money to be spent: "))
            break
        except ValueError:
            print("INVALID! Please re-enter.")

    # selecting items
    selected_items = []
    while True:
        try:
            selected_item_number = int(input("\nPlease enter the item number of the item that you desire: "))
            print(f'\nNOTE: Select however many items you would like to purchase, once you are done selecting, please enter the number 0 to proceed.')
            if selected_item_number == 0:
                break
            elif selected_item_number in [num for cat in items.values() for num in cat.keys()]:
                selected_items.append(selected_item_number)
            else:
                print("Invalid item number. Please re-enter.")
        except ValueError:
            print("INVALID, Please enter a valid item number.")

    total_price = 0
    for selected_item_number in selected_items:
        for category, category_items in items.items():
            if selected_item_number in category_items:
                selected_item = category_items[selected_item_number]['item']
                price = category_items[selected_item_number]['price']
                print(f"\nYou selected {selected_item.capitalize()} - Price: {price} AED. Your item is now being dispensed.")
                total_price += price

    if money >= total_price:
        change = money - total_price
        print(f"\nYour total is: {total_price} AED")
        print(f"You will receive {change} AED in change.")
    else:
        print(f"\nYour total is: {total_price} AED")
        print(f"Sorry, you don't have enough money.")

else:
    print("Apologies, you must be of age in order to purchase our products.")
    