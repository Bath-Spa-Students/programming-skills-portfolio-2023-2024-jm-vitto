# Make a list of sandwich orders
sandwich_orders = ["tuna", "club", "pastrami", "chicken", "vegetarian"]

# Make an empty list for finished sandwiches
finished_sandwiches = []

# Loop through sandwich orders
while sandwich_orders:
    # Make each sandwich
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    # Move the made sandwich to finished sandwiches
    finished_sandwiches.append(current_sandwich)

# Print the list of finished sandwiches
print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich.capitalize())
