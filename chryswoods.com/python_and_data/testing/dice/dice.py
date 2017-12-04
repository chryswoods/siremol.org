"""
This module provides a class for a fair, n-sided dice.

Author - Lester Hedges
"""

import random

class Dice():
    """ A simple class for an n-sided fair dice. """

    def __init__(self, n = 6, seed = None):
        """ Construct a n-sided dice.

            n -- The number of sides on the dice.
        """

        if not type(n) is int:
            raise TypeError("The number of sides must be of type 'int'!")

        if n < 0:
            raise ValueError("The number of sides cannot be negative!")

        # Seed the random number generator.
        if seed is None:
            random.seed()
        else:
            random.seed(seed)

        # Set the number of sides.
        self._n = n

        # Initialise the value of the last dice roll.
        self._last_roll = None

    def sides(self):
        """ Return number of sides of the dice. """
        return self._n

    def lastRoll(self):
        """ Return the value of the last dice roll. """
        return self._last_roll

    def roll(self):
        """ Roll the dice and return its value. """

        # Generate a random value between 1 and n inclusive.
        value = random.randint(1, self._n)

        # Store the value of the roll.
        self._last_roll = value

        # Return the value.
        return value

