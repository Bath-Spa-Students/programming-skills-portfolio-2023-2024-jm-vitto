# List of places known for specific philosophies
places_to_visit = [
    "Kyoto, Japan (Zen Buddhism)",
    "Athens, Greece (Ancient Philosophy)",
    "Varanasi, India (Hinduism)",
    "Rome, Italy (Stoicism)",
    "Beijing, China (Daoism)"
]

# Print the list in its original order vertically
print("Original order:")
for place in places_to_visit:
    print(place)

# Print a blank line for separation
print()

# Print the list in alphabetical order vertically without modifying the actual list
print("Sorted in alphabetical order:")
for place in sorted(places_to_visit):
    print(place)

# Print a blank line for separation
print()

# Print the list to show it's still in its original order vertically
print("Original order (still intact):")
for place in places_to_visit:
    print(place)

# Print a blank line for separation
print()

# Print the list in reverse alphabetical order vertically without changing the original list
print("Sorted in reverse alphabetical order:")
for place in sorted(places_to_visit, reverse=True):
    print(place)

# Print a blank line for separation
print()

# Print the list to show it's still in its original order vertically
print("Original order (still intact):")
for place in places_to_visit:
    print(place)

# Print a blank line for separation
print()

# Change the order of the list using reverse() and print it vertically
places_to_visit.reverse()
print("Reversed order:")
for place in places_to_visit:
    print(place)

# Print a blank line for separation
print()

# Change the order of the list again to revert it to its original order and print it vertically
places_to_visit.reverse()
print("Back to original order:")
for place in places_to_visit:
    print(place)

# Print a blank line for separation
print()

# Change the order of the list using sort() to store it in alphabetical order and print it vertically
places_to_visit.sort()
print("Sorted in alphabetical order:")
for place in places_to_visit:
    print(place)

# Print a blank line for separation
print()

# Change the order of the list using sort() to store it in reverse alphabetical order and print it vertically
places_to_visit.sort(reverse=True)
print("Sorted in reverse alphabetical order:")
for place in places_to_visit:
    print(place)
