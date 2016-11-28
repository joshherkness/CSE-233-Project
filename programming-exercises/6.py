# Program 3.6
# 
# 1. Prompt the user for a month, day, and two digit year
# 2. If the date * month = year, the date is magic! Print that.
# 3. Otherwise, the date is not magic :( Print that.

def main():

	# Ask for day, month, year.
	month = int(input('Enter a month: '))
	day = int(input('Enter a day: '))
	year = int(input('Enter a year (Ex: 16): '))

	# Determine if the day is magic.
	if month * day == year:
		print('That day is magic!!! :D')
	else:
		print('That day isn\'t magic... :(')

main()