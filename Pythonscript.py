# Midterm Programming Project

# Variables

game_name = "GTA V" # This is the game variable
price = 59.99 # The price of GTA that will be used later in a calculation

# Adding a user input for an email and the amount of game copies the person wants to purchase

user_email = input("Please enter your email: ")
game_count = input("How many copies of GTA V would you like?: ")

# Convert game_count input to a number

count = int(game_count)

# First calculation

subtotal = count * price

# Using if and else statements to apply a discount

if count >= 3:
    discount = 9.99
    print("You saved $9.99 on this order for a bulk deal!")
elif count == 2:
    discount = 5.99
    print("You saved $5.99 on this duo deal!")
else:
    discount = 0.00
    print("No savings today!")

# Second calculation

total = subtotal - discount

# Print receipt for customer

print("\n---ORDER CONFIRMATION---")
print("The code(s) has been sent to your email:", user_email)
print("Game Purchased:", game_name)
print("Number of copies purchased:", count)
print("Subtotal: $", subtotal)
print("Discount: $", discount)
print("Amount Due: $", total)
print("Thank you for your purchase!")