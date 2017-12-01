import pytest

from ..dice import Dice

@pytest.mark.parametrize("sides, rolls", [(6, 100000), (12, 100000)])
def test_average(sides, rolls):
    """ Test that the average dice roll is correct. """

    # Initialise the dice object.
    dice = Dice(sides)

    # Work out the expected average roll.
    exp = sum(range(1, sides+1)) / sides

    # Calculate the sum of the dice rolls.
    total = 0
    for i in range(0, rolls):
        total += dice.roll()

    # Check that the average matches the expected value.
    average = total / rolls
    assert average == pytest.approx(exp, rel=1e-2)

@pytest.mark.parametrize("sides, rolls", [(6, 1000000), (12, 1000000)])
def test_fair(sides, rolls):
    """ Test that a dice is fair. """

    # Initialise the dice object.
    dice = Dice(sides)

    # Create a dictionary to hold the tally for each outcome.
    tally = {}
    for i in range(1, sides+1):
        tally[i] = 0

    # Roll the dice 'rolls' times.
    for i in range(0, rolls):
        tally[dice.roll()] += 1

    # Assert that the probability is correct.
    for i in range(1, sides):
        assert tally[i] / rolls == pytest.approx(1 / sides, 1e-2)

def test_double_roll():
    """ Check that the probability for the sum of two six-sided dice matches
        the expected distribution.
    """

    # Expected probabilities for the sum of two dice.
    # For two n-sided dice, the probability of two rolls summing to x is
    # (n − |x−(n+1)|) / n^2, for x = 2 to 2n.
