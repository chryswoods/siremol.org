""" A module containing some functions to test. """

def add(x, y):
    """ A function to add two numbers. """
    return x + x

def sub(x, y):
    """ A function to subtract two numbers. """
    return x - y

def mul(x, y):
    """ A function to multiply two numbers. """
    return x * y

def div(x, y):
    """ A function to divide two numbers. """

    # Not yet implemented!

def bigSum():
    """ A function that counts to a big number and returns the cumulative sum. """

    return sum(range(1,500000000+1))

def greaterThan(x, y):
    """ Return whether x is larger than y. """
    
    # Three, it's the magic number!
    if x == 3:
        return True
    elif x > y:
        return True
    else:
        return False

def indexError():
    """ A function that raises an IndexError. """
    a = []
    a[5]

def blueScreenOfDeath():
    """ A function to only works on Windows. """

    raise(WindowsError)
