# Program 3.7
#
# 1. User enters two primary colors.
# 2. Output secondary color that results from mixing the two colors.
#
# WARNING: Very terrible programming ahead.
# However, we wanted to show the use of decision structures to complete the task.

def main():
    possible_colors = ['red', 'blue', 'yellow']
    # Prompt user for colors
    c1 = input('Enter either red, blue, or yellow: ')
    c2 = input('Enter either red, blue, or yellow: ')
    # Ensure that the colors are valid before mixing.
    if (c1 in possible_colors and c2 in possible_colors):
        print(mix(c1, c2))
    else:
        # Error message
        print('You fool!  You didn\'t enter valid colors.')

# Function that takes in two colors, and provies the resulting
# secondary color after mixed together.
def mix(c1, c2):
    if (c1 == c2):
        return c1
    elif (c1.lower() == 'red' or c2.lower() == 'red'):
        if (c1.lower() == 'blue' or c2.lower() == 'blue'):
            return 'violet'
        elif (c1.lower() == 'yellow' or c2.lower() == 'yellow'):
            return 'orange'
    elif (c1.lower() == 'blue' or c2.lower() == 'blue'):
        if (c1.lower() == 'red' or c2.lower() == 'red'):
            return 'violet'
        elif (c1.lower() == 'yellow' or c2.lower() == 'yellow'):
            return 'green'
    elif (c1.lower() == 'yellow' or c2.lower() == 'yellow'):
        if (c1.lower() == 'red' or c2.lower() == 'red'):
            return 'orange'
        elif (c1.lower() == 'blue' or c2.lower() == 'blue'):
            return 'green'
main()
