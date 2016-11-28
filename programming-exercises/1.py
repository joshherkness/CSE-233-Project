# Program 3.1
#
# 1. Enter a number between 1 and 7 inclusive.
# 2. Print the corresponding day of the week, or error.

def main():
    day = int(input('Enter a number in the range of 1 through 7: '))
    if (day == 1):
        print('You entered a day that corresponds to', 'Monday')
    elif (day == 2):
        print('You entered a day that corresponds to', 'Tuesday')
    elif (day == 3):
        print('You entered a day that corresponds to', 'Wednesday')
    elif (day == 4):
        print('You entered a day that corresponds to', 'Thursday')
    elif (day == 5):
        print('You entered a day that corresponds to', 'Friday')
    elif (day == 6):
        print('You entered a day that corresponds to', 'Saturday')
    elif (day == 7):
        print('You entered a day that corresponds to', 'Sunday')
    else:
        print('You fool!  You didn\'t enter a number in the correct range!')
main()
