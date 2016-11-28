# Program 3.8
# 
# Knowing that hot dogs come in packages of 10, and buns come 
# in packages of 8.
# 
# 1. Prompt the user for the number of people eating.
# 2. Prompt the user for the amount of hot dogs per person.
# 3. Print:
# 	- The minimum number of packages of hot dogs required.
# 	- The minimum number of packages of hot dog buns requires.
# 	- The number of hot dogs that will be left over.
# 	- The number of hot dog buns that will be left over.

from math import ceil

def main():

	# Get the inputs
	num_of_people = int(input('How many people are there going to be?: '))
	serving_size = int(input('How many hot dogs per person?: '))
	hot_dogs = num_of_people * serving_size

	# Now we do some math
	min_hot_dog_packages = ceil(hot_dogs / 10)
	min_hot_dog_bun_packages = ceil(hot_dogs / 8)
	left_over_hot_dogs = (min_hot_dog_packages * 10) - hot_dogs
	left_over_hot_dog_buns = (min_hot_dog_bun_packages * 8) - hot_dogs

	# Let's print some stuff
	print('Minimum number of packages of hot dogs required:', min_hot_dog_packages)
	print('Minimum number of packages of hot dog buns required:', min_hot_dog_bun_packages)
	print('Left over hot dogs:', left_over_hot_dogs)
	print('Left over hot dog buns:', left_over_hot_dog_buns)

main()