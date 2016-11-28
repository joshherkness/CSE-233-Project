# Program 3.14
# 
# 1. Prompt the user for their height in inches, and weight in pounds.
# 2. Display the persons BMI, and whether they are optimal weight,
#    overweight, or underweight.

def main():

	# Get the users stats
	weight = eval(input('Enter your weight (in pounds): '))
	height = eval(input('Enter your height (in inches): '))

	# Calculate BMI
	bmi = weight * (703 / (height ** 2))

	# Display results
	if bmi > 25:
		print('You\'re overweight')
	elif bmi < 18.5:
		print('You\'re underweight')
	else:
		print('You\'re optimal weight')
main()