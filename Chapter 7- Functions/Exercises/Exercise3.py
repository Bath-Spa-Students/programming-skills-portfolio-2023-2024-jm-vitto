def make_shirt(size, message):
    print(f"This shirt is {size} and always remember, '{message}'.")

while True:
    # Get input from user for size and message
    size = input("Enter the size of the shirt: ")
    message = input("Enter the message to be printed on the shirt: ")

    # Call the function using positional arguments with user input
    make_shirt(size, message)

    # Ask user if they want to continue
    choice = input("Do you want to continue making shirts? (yes/no): ")
    if choice.lower() != "yes":
        print("Thank you, enjoy!!")
        break
