import math


def split_check(total, number_of_people):
    if number_of_people <= 1:
        raise ValueError("More than 1 person is required to split the check!")
    return math.ceil(total / number_of_people)


try:
    total_due = float(input("What's the total "))
    total_people = int(input("How many people? "))
    amount_due = split_check(total_due, total_people)

except ValueError as err:
    print ("Oh no! Invalid number. Please try again")
    print ("({})".format(err))

except NameError:
    print ("Oh no! Invalid number. Please try again")

else:
    print ("Each person owes ${}".format(amount_due))

########################################################

"""
This is importing a function named `tweet` from a file
    that we unfortunately don't have access to change.

You use it like so:
>>> tweet("Hello this is my tweet")

If the function cannot connect to Twitter,
    the function will raise a `CommunicationError`
If the message is too long,
    the function will raise a `MessageTooLongError`
"""
from twitter import (
    tweet,
    MessageTooLongError,
    CommunicationError,
)


message = input("What would you like to tweet?  ")
# Your code here



