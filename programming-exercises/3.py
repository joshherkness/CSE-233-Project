# Program 3.3
#
# 1. Enter age
# 2. Given the constraints, print if they are a baby, child, teenager, or adult.

def main():
    age = int(input('Enter your age (in years): '))
	if age <= 1:
	    print('Baby 👶')
	elif age > 1 and age < 13:
	    print('Child 😣')
	elif age >= 13 and age < 20:
	    print('Teenager 😎')
	elif age >=20:
	    print('Adult 😴')
	else:
	    print('You must not be born yet 😘')
main()
