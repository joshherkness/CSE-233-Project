# Program 3.5
#
# 1. Prompt user for mass
# 2. Calculate weight
# 3. Print if the object is too heavy (>500) or too light (<100)

def main():
    # Prompt user for mass of an object
    mass = eval(input('Enter an objects mass: '))
    # Calculate weight
    weight = mass * 9.8
    print('The object has a weight of', weight)

    if (weight > 500):
        print('The object is too heavy (>500).')
    elif (weight < 100):
        print('The object is too light (<100).')
main()
