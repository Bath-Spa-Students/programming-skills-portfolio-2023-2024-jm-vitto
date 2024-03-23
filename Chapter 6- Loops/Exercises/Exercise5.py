# Make a list of sandwich orders
sandwich_orders = ["tuna", "club", "pastrami", "chicken", "pastrami", "vegetarian", "pastrami"]

# Make an empty list for finished sandwiches
finished_sandwiches = []

# Initialize a count for pastrami sandwiches made
pastrami_count = 0

# Loop through sandwich orders
while sandwich_orders:
    # Make each sandwich
    current_sandwich = sandwich_orders.pop(0)
    if current_sandwich == 'pastrami':
        pastrami_count += 1
        if pastrami_count == 3:
            print("Sorry, the deli has run out of pastrami.")
            continue  # Skip making the current pastrami sandwich
    print(f"I made your {current_sandwich} sandwich.")
    # Move the made sandwich to finished sandwiches
    finished_sandwiches.append(current_sandwich)

# Print the list of finished sandwiches
print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich.capitalize())
