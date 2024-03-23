# Set the predefined age
predefined_age = 30

# Ask the user if they agree with the predefined age
agree = input("Do you agree with the predefined age? (yes/no): ")

if agree.lower() == 'yes':
    age = predefined_age
else:
    age = int(input("Please enter your age: "))

# Determine the person's stage of life
if age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")
