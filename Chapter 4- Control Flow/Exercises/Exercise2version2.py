import random

# Set the alien's color to something other than green
alien_color = 'yellow'  # Change this to 'red' to test the else block

if alien_color == 'green':
    print("Congratulations! You just earned 5 points for shooting the green alien.")
else:
    print("Congratulations! You just earned 10 points for shooting the non-green alien.")
