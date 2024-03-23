# Define a dictionary with Stoics and their preferred type of pizza
stoics_pizza_preference = {
    "Epictetus": "Margherita",
    "Marcus Aurelius": "Neapolitan",
    "Seneca": "Pepperoni",
    "Musonius Rufus": "Vegetarian",
    "Zeno of Citium": "Hawaiian"
}

# Loop through the dictionary and prompt the user for pizza toppings
for stoic, pizza_preference in stoics_pizza_preference.items():
    print(f"{stoic} would enjoy a {pizza_preference} pizza.")

# Prompt the user to enter pizza toppings
print("\nEnter your pizza toppings (enter 'quit' to finish):")
while True:
    topping = input("Enter topping: ")
    if topping.lower() == 'quit':
        break
    print(f"You'll add {topping} to your pizza.")
