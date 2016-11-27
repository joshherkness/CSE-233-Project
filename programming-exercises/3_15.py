# Program 3.15
#
# 1. Input seconds
# 2. Output seconds in correct format.

def main():
    # Prompt user for seconds input.
    seconds = eval(input('Enter a number in seconds: '))

    # Output in desired format.
    if (seconds >= 60 and seconds < 3600):
        m, s = seconds_to_minutes(seconds)
        print(m, 'minute(s),', s, 'seconds')
    elif (seconds >= 3600 and seconds < 86400):
        h, s = seconds_to_hours(seconds)
        print(h, 'hour(s),', s, 'seconds')
    elif (seconds >= 86400):
        d, s = seconds_to_days(seconds)
        print(d, 'day(s),', s, 'seconds')
    else:
        # Error message
        print('C\'mon man, it\'s not that hard.')

# Helper functions

def seconds_to_minutes(seconds):
    return divmod(seconds, 60)

def seconds_to_hours(seconds):
    return divmod(seconds, 3600)

def seconds_to_days(seconds):
    return divmod(seconds, 86400)

main()
