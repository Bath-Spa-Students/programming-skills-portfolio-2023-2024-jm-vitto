import random

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "How do you organize a space party? You planet!",
    "What did one plate say to the other plate? Lunch is on me!",
    "Why did the bicycle fall over? Because it was two-tired!",
    "What do you call fake spaghetti? An impasta!",
    "Why don't skeletons fight each other? They don't have the guts!",
    "What did the grape say when it got stepped on? Nothing, it just let out a little wine!",
    "Why couldn't the leopard play hide and seek? Because he was always spotted!"
]

print("Get ready for some jokes! Press Ctrl-C to stop.")

while True:
    print(random.choice(jokes))
