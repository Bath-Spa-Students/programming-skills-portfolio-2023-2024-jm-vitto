def make_shirt(size="large", message="I love Python"):
    print(f"This shirt is {size} and always remember, '{message}'.")

# Call the function to make a large shirt with the default message
make_shirt()

# Call the function to make a medium shirt with the default message
make_shirt(size="medium")

# Loop for making additional shirts
while True:
    # Ask user if they want to continue
    choice = input("Do you want to continue making shirts? (yes/no): ")
    if choice.lower() == "no":
        print("Thank you, enjoy!!")
        break
    elif choice.lower() != "yes":
        print("Invalid choice! Please enter 'yes' or 'no'.")
        continue

    # Get input from user for size and message
    size_input = input("Enter the size of the shirt: ")
    message_input = input("Enter the message to be printed on the shirt: ")

    # Call the function to make a shirt with user input
    make_shirt(size=size_input, message=message_input)
