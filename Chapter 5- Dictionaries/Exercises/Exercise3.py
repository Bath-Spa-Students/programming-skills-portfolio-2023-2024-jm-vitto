# Define the initial glossary with programming terms and their meanings
glossary = {
    "variable": "A named storage location in a program, used to store data that can be referenced and manipulated.",
    "function": "A block of organized, reusable code that performs a specific task.",
    "loop": "A programming construct that repeats a block of code as long as a specified condition is true.",
    "conditional statement": "A statement that performs different actions depending on whether a condition is true or false.",
    "algorithm": "A set of well-defined instructions for solving a problem or performing a task in a finite number of steps."
}

# Add five more Python terms to the glossary
glossary.update({
    "list": "A collection of items that can be accessed and manipulated individually.",
    "dictionary": "A collection of key-value pairs, where each key is associated with a value.",
    "tuple": "An immutable collection of items, often used for storing related data.",
    "set": "An unordered collection of unique items, used for tasks such as membership testing and eliminating duplicates.",
    "slice": "A way to select a subset of items from a sequence, such as a list or a string."
})

# Print each word and its meaning using a loop
for word, meaning in glossary.items():
    print(word.capitalize() + ":")
    print(meaning)
    print()  # Insert a blank line between each word-meaning pair
