# Program 3.4
# 
# 1. Prompt the user for a number.
# 2. Display the Roman numeral version of the number.
# 3. If the number is outside the range 0 to 10, display an 
#    error message.

def main():

	# Define a dictionary of Roman numerals because we can...
	rn = { 
		1:'I', 
		2:'II', 
		3:'III', 
		4:'IV', 
		5:'V', 
		6:'VI', 
		7:'VII', 
		8:'VIII', 
		9:'IX',
		10:'X'
	}

	# Ask for the user's input.
	num = int(input('Enter a number between 1 and 10: '))

	# Print either a Roman numeral or an error message.
	if num in rn:
		print(rn[num])
	else:
		print('Sorry, that number is out of range...')

main()