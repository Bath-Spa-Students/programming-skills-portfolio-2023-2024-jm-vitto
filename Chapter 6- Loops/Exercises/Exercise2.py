while True:
    age = input("Please enter your age (enter 'quit' to exit): ")
    if age.lower() == 'quit':
        break
    
    age = int(age)  # Convert age to an integer
    
    if age < 3:
        print("Your ticket is free!")
    elif 3 <= age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")
