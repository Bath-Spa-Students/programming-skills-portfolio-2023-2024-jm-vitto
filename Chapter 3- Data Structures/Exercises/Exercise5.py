# List of Stoics to invite to dinner
stoics_to_invite = ["Epictetus", "Seneca", "Marcus Aurelius"]

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

# Print the name of the guest who can't make it
guest_cant_make_it = "Epictetus"
print(f"Unfortunately, {guest_cant_make_it} can't make it to dinner.\n")

# Ensure stoics_to_invite is a list before removing an element
if isinstance(stoics_to_invite, list):
    # Replace the guest who can't make it with a new person
    stoics_to_invite.remove(guest_cant_make_it)
    new_guest = "Cicero"  # New person to invite
    stoics_to_invite.append(new_guest)

# Print a second set of invitation messages to remaining guests
print("Second set of invitation messages:")
for stoic in stoics_to_invite:
    print(f"Dear {stoic},\n\nYou are cordially invited to dinner at my place. It would be an honor to have you join us for an evening of philosophical discussions and camaraderie.\n\nI admire {stoics_interesting_traits[stoic]}\n\nPlease let me know if you can make it.\n\nBest regards,\nJohn Mhelvs Vitto")
    print("\n" + "-"*50 + "\n")  # Add a line for separation
