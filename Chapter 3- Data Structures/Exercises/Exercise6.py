# List of Stoics to invite to dinner
stoics_to_invite = ["Seneca", "Marcus Aurelius", "Cicero"]

# Dictionary of Stoics with their interesting traits
stoics_interesting_traits = {
    "Epictetus": "Your resilience and wisdom in the face of adversity have inspired countless individuals to lead better lives.",
    "Seneca": "Your profound insights into human nature and your emphasis on virtue have left an indelible mark on Stoic philosophy.",
    "Marcus Aurelius": "As a philosopher-king, your reflections on life, leadership, and virtue in 'Meditations' continue to guide and inspire readers worldwide.",
    "Cicero": "Your eloquent writings on ethics and philosophy have greatly influenced Western thought."
}

# Print invitation messages to each Stoic
for stoic in stoics_to_invite:
    print(f"Dear {stoic},\n\nYou are cordially invited to dinner at my place. It would be an honor to have you join us for an evening of philosophical discussions and camaraderie.\n\nI admire {stoics_interesting_traits[stoic]}\n\nPlease let me know if you can make it.\n\nBest regards,\nJohn Mhelvs Vitto")
    print("\n" + "-"*50 + "\n")  # Add a line for separation

# Print a message saying that only two people can be invited for dinner
print("Unfortunately, the dinner table won't arrive in time for the dinner, so I can only invite two people for dinner.\n")

# Remove guests from the list one at a time until only two names remain
while len(stoics_to_invite) > 2:
    removed_guest = stoics_to_invite.pop()
    print(f"Sorry {removed_guest}, I can't invite you to dinner anymore.")

# Print a message to the remaining two people still on the list, letting them know they're still invited
print("\nInvitations to the remaining guests:")
for stoic in stoics_to_invite:
    print(f"Dear {stoic},\n\nYou're still invited to dinner at my place. I look forward to your company.\n\nBest regards,\nJohn Mhelvs Vitto")
    print("\n" + "-"*50 + "\n")  # Add a line for separation

# Use del to remove the last two names from the list
del stoics_to_invite[:]
print("The list is now empty:", stoics_to_invite)
