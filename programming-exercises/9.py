# Program 3.9
#
# 1. Input the number of a roulette pocket in the range 0 to 36 inclusive.
# 2. output the corresponding pocket color.
#
# NOTE: The use of range() function to accommodate even/odd number in certain ranges.

def main():
    # Prompt user for pocket number.
    pocket = int(input('Enter the number of a pocket between 0 and 36 (inclusive): '))

    # Validate using a decision statement.
    if (pocket in range(0, 37)):
        print('The pocket is', pocket_color(pocket))
    else:
        print('You fool!  You didn\'t enter a number in the correct range.')

# Function that returns the color of a pocket, given
# only the pocket number.
def pocket_color(pocket):
    if (pocket == 0):
        return 'green'
    elif (pocket in range(1, 11, 2)):
        return 'red'
    elif (pocket in range(2, 11, 2)):
        return 'black'
    elif (pocket in range(11, 19, 2)):
        return 'black'
    elif (pocket in range(12, 19, 2)):
        return 'red'
    elif (pocket in range(19, 29, 2)):
        return 'red'
    elif (pocket in range(20, 29, 2)):
        return 'black'
    elif (pocket in range(29, 37, 2)):
        return 'black'
    elif (pocket in range(30, 37, 2)):
        return 'red'
    else: return None
main()
