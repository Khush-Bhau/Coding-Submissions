def is_leap(year):
    # Check if the year is a leap year based on the given conditions
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# The provided code stub reads from STDIN and passes arguments to the is_leap function.
# You do not need to modify the code stub below this comment.

