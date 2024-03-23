import random

# Randomly select the alien's color
alien_color = random.choice(['green', 'yellow', 'red'])

if alien_color == 'green':
    print("Congratulations! You just earned 5 points for shooting the green alien.")
else:
    print("Congratulations! You just earned 10 points for shooting the non-green alien.")
