# The girl's budget for buying USB sticks
total_money = 50

# Cost of a single USB stick
usb_stick_cost = 6

# Calculate how many USB sticks she can buy with her budget
num_usb_sticks = total_money // usb_stick_cost

# Calculate the remaining money after buying as many USB sticks as possible
money_left = total_money % usb_stick_cost

# Display how many USB sticks she can buy
print("With £", total_money, ", you can buy:")

# Display the number of USB sticks she can buy
print("USB Sticks: ", num_usb_sticks)

# Display the remaining money after buying USB sticks
print("Money Left: £", money_left)
