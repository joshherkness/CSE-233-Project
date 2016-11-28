# Program 3.12
# 
# 1. Prompt the user to enter the number of packages being ordered
# 2. Display the quantity discount

def main():

	# Get the number of packages
	packages = int(input('Enter the number of packages ordered: '))

	# Display the discount
	if packages >= 10 and packages <= 19:
		print('Discount: 10%')
	elif packages >= 20 and packages <=49:
		print('Discount: 20%')
	elif packages >= 50 and packages <= 99:
		print('Discount: 30%')
	elif packages >= 100:
		print('Discount: 40%')

main()