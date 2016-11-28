# Program 3.10
# 
# 1. Prompt the user for the number of pennies, nickels, 
#    dimes, and quarters.
# 2. Display a message indicating if the amount entered 
#  - Is greater than $1.00
#  - Equals $1.00
#  - Is less than $1.00

def main():
	
	# Get the inputs
	pennies = int(input('Enter the number of pennies: '))
	nickels = int(input('Enter the number of nickels: '))
	dimes = int(input('Enter the number of dimes: '))
	quarters = int(input('Enter the number of quarters: '))

	# Calculate the amount
	amount = pennies * 0.01 + nickels * 0.05 + dimes * 0.1 + quarters * 0.25

	# Display the results
	if amount > 1.0:
		print('The amount was too high...')
	elif amount < 1.0:
		print('The amount was too low...')
	else:
		print('Congratulations!!! You win!')
main()