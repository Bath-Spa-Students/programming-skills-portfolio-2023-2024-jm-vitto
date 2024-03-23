# Create dictionaries for each pet associated with a Stoic and additional information
koala = {"animal": "koala", "owner": "Epictetus", "good_to_have": "Koalas are gentle and easy to care for, making them great companions for those seeking peace and tranquility."}
lion = {"animal": "lion", "owner": "Marcus Aurelius", "good_to_have": "Lions are symbols of strength and courage, serving as powerful reminders of resilience and fortitude."}
golden_retriever = {"animal": "golden retriever", "owner": "Seneca", "good_to_have": "Golden retrievers are loyal and affectionate, offering unwavering companionship and emotional support to their owners."}
red_panda = {"animal": "red panda", "owner": "Musonius Rufus", "good_to_have": "Red pandas are playful and curious, bringing joy and laughter into the lives of those who care for them."}
otter = {"animal": "otter", "owner": "Zeno of Citium", "good_to_have": "Otters are social and intelligent animals, fostering connections and promoting a sense of community among their human companions."}

# Store the dictionaries in a list called pets
pets = [koala, lion, golden_retriever, red_panda, otter]

# Loop through the list and print information about each pet and its Stoic owner
for pet in pets:
    print(f"Animal: {pet['animal'].capitalize()}")
    print(f"Owner: {pet['owner'].capitalize()} (Stoic)")
    print(f"Description: {pet['good_to_have']}")
    print()  # Insert a blank line between each pet's information
