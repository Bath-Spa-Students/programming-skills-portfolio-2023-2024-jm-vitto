# Define a dictionary with major rivers and the countries they run through
rivers = {
    "Nile": "Egypt",
    "Amazon": "Brazil",
    "Yangtze": "China"
}

# Print a sentence about each river
print("Information about major rivers:")
for river, country in rivers.items():
    print(f"The {river} runs through {country}.")

# Print the name of each river
print("\nList of major rivers:")
for river in rivers:
    print(river)

# Print the name of each country
print("\nList of countries with major rivers:")
for country in rivers.values():
    print(country)
