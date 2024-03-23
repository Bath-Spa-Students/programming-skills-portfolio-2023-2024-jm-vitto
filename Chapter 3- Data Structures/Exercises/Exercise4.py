# Dictionary of Stoics with their interesting traits
stoics_to_invite = {
    "Epictetus": "Your resilience and wisdom in the face of adversity have inspired countless individuals to lead better lives.",
    "Seneca": "Your profound insights into human nature and your emphasis on virtue have left an indelible mark on Stoic philosophy.",
    "Marcus Aurelius": "As a philosopher-king, your reflections on life, leadership, and virtue in 'Meditations' continue to guide and inspire readers worldwide."
}

# Print invitation messages to each Stoic
for stoic in stoics_to_invite:
    print(f"Dear {stoic},\n\nYou are cordially invited to dinner at my place. It would be an honor to have you join us for an evening of philosophical discussions and camaraderie.\n\nI admire {stoics_to_invite[stoic]}\n\nPlease let me know if you can make it.\n\nBest regards,\nJohn Mhelvs Vitto")
    print("\n" + "-"*50 + "\n")  # Add a line for separation
