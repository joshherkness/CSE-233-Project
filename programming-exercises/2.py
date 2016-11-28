# Program 3.2
# 
# 1. Ask for the length and width of two rectangles
# 2. Tell the user which rectangle is bigger, or if they are 
#    the same.

def main():

	# Get the inputs
	len_1 = eval(input('Enter the length of Rectangle #1: '))
	wid_1 = eval(input('Enter the width of Rectangle #1: '))
	len_2 = eval(input('Enter the length of Rectangle #2: '))
	wid_2 = eval(input('Enter the width of Rectangle #2: '))

	# Compute the area
	area_1 = len_1 * wid_1
	area_2 = len_2 * wid_2

	# Inform the user
	if area_1 > area_2:
		print('Rectangle #1 is bigger')
	elif area_2 > area_1:
		print('Rectangle #2 is bigger')
	else:
		print('The rectangles have the same area')

main()