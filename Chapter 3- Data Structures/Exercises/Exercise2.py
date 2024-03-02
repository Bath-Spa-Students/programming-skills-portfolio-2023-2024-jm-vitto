# Store the names of famous Stoics in a list called stoics
stoics = ["Epictetus", "Seneca", "Marcus Aurelius", "Zeno of Citium", "Cato the Younger"]

# Define Stoic quotes
stoic_quotes = {
    "Epictetus": "It's not what happens to you, but how you react to it that matters.",
    "Seneca": "Luck is what happens when preparation meets opportunity.",
    "Marcus Aurelius": "The happiness of your life depends upon the quality of your thoughts.",
    "Zeno of Citium": "Well-being is attained by little and little, and nevertheless is no little thing itself.",
    "Cato the Younger": "He who lives in harmony with himself lives in harmony with the universe."
}

# Print personalized messages with Stoic quotes for each Stoic in the list
for stoic in stoics:
    print(f"Hey {stoic}, just wanted to share a Stoic quote with you:")
    print(stoic_quotes[stoic])
    print("-" * 30)  # Add a line for separation
