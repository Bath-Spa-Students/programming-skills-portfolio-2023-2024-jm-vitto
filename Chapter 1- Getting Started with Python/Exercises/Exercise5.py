# Calculating the area of a circle from a given radius

import math

# Accept the radius of the circle from the user
radius = float(input("Enter the radius of the circle: "))

# Compute the area of the circle
area = math.pi * radius ** 2

# Print the area of the circle
print("The area of the circle with radius", radius, "is:", area)
