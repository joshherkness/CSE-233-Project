# Program 3.13
#
# 1. Prompt user for weight of package.
# 2. Output corresponding shipping charge.

def main():
    # Prompt user for weight of package.
    weight = eval(input('Enter the weight of your package: '))
    # Output corresponding shipping charge.
    print('Shipping charges:', shipping_charge(weight))

# Function calculates the corresponding shipping charge
# for a given weight.
def shipping_charge(weight):
    rate_per_pound = 0;
    if (weight <= 2.0):
        rate_per_pound = 1.50
    elif (weight > 2.0 and weight <= 6.0):
        rate_per_pound = 3.00
    elif (weight > 6.0 and weight <= 10.0):
        rate_per_pound = 4.00
    elif (weight > 10.0):
        rate_per_pound = 4.75
    return weight * rate_per_pound

main()
