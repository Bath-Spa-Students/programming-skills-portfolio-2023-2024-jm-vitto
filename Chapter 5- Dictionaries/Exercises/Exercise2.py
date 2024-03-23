# Define a glossary with programming terms and their meanings
glossary = {
    "variable": "A named storage location in a program, used to store data that can be referenced and manipulated.",
    "function": "A block of organized, reusable code that performs a specific task.",
    "loop": "A programming construct that repeats a block of code as long as a specified condition is true.",
    "conditional statement": "A statement that performs different actions depending on whether a condition is true or false.",
    "algorithm": "A set of well-defined instructions for solving a problem or performing a task in a finite number of steps."
}

# Print each word and its meaning as neatly formatted output
for word, meaning in glossary.items():
    print(word.capitalize() + ":")
    print(meaning)
    print()  # Insert a blank line between each word-meaning pair
