# Program 3.11
#
# 1. Input amount of books that you purchased this month.
# 2. Output corresponding amount of points awarded.

def main():
    books = int(input('Enter the number of books that you purchased this month: '))
    print('You have been awarded', points_awarded(books), 'points.')

def points_awarded(books):
    if (books == 0):
        return 0
    elif (books == 2):
        return 5
    elif (books == 4):
        return 15
    elif (books == 6):
        return 30
    elif (books >= 8):
        return 60
    else: return None
main()
