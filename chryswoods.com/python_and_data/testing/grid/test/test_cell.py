from ..grid import Cell

def test_bulk():
    """ Test that a cell in the bulk of the grid is correct. """

    # Instantiate a cell in the bulk of a 10x10 grid.
    c = Cell(4, 4, 10, 10)

    # Make sure that the cell has 4 neighbours.
    assert c.neighbours() == 4

    # Check the coordinates of the neighbours.
    assert c.left()  == (3, 4)
    assert c.right() == (5, 4)
    assert c.up()    == (4, 5)
    assert c.down()  == (4, 3)

def test_left_edge():
    """ Test that a cell on the left edge of the grid is correct. """

    # Instantiate a cell on the left edge of a 10x10 grid.
    c = Cell(0, 4, 10, 10)

    # Make sure that the cell has 3 neighbours.
    assert c.neighbours() == 3

    # Check the coordinates of the neighbours.
    assert c.left()  == (None, 4)
    assert c.right() == (1, 4)
    assert c.up()    == (0, 5)
    assert c.down()  == (0, 3)

def test_right_edge():
    """ Test that a cell on the right edge of the grid is correct. """

    # Instantiate a cell on the right edge of a 10x10 grid.
    c = Cell(9, 4, 10, 10)

    # Make sure that the cell has 3 neighbours.
    assert c.neighbours() == 3

    # Check the coordinates of the neighbours.
    assert c.left()  == (8, 4)
    assert c.right() == (None, 4)
    assert c.up()    == (9, 5)
    assert c.down()  == (9, 3)

def test_bottom_edge():
    """ Test that a cell on the bottom edge of the grid is correct. """

    # Instantiate a cell on the bottom edge of a 10x10 grid.
    c = Cell(4, 0, 10, 10)

    # Make sure that the cell has 3 neighbours.
    assert c.neighbours() == 3

    # Check the coordinates of the neighbours.
    assert c.left()  == (3, 0)
    assert c.right() == (5, 0)
    assert c.up()    == (4, 1)
    assert c.down()  == (4, None)

def test_top_edge():
    """ Test that a cell on the top edge of the grid is correct. """

    # Instantiate a cell on the top edge of a 10x10 grid.
    c = Cell(4, 9, 10, 10)

    # Make sure that the cell has 3 neighbours.
    assert c.neighbours() == 3

    # Check the coordinates of the neighbours.
    assert c.left()  == (3, 9)
    assert c.right() == (5, 9)
    assert c.up()    == (4, None)
    assert c.down()  == (4, 8)

def test_bottom_left_corner():
    """ Test that a cell on the bottom left corner of the grid is correct. """

    # Instantiate a cell on the bottom left corner of a 10x10 grid.
    c = Cell(0, 0, 10, 10)

    # Make sure that the cell has 2 neighbours.
    assert c.neighbours() == 2

    # Check the coordinates of the neighbours.
    assert c.left()  == (None, 0)
    assert c.right() == (1, 0)
    assert c.up()    == (0, 1)
    assert c.down()  == (0, None)

def test_bottom_right_corner():
    """ Test that a cell on the bottom right corner of the grid is correct. """

    # Instantiate a cell on the bottom right corner of a 10x10 grid.
    c = Cell(9, 0, 10, 10)

    # Make sure that the cell has 2 neighbours.
    assert c.neighbours() == 2

    # Check the coordinates of the neighbours.
    assert c.left()  == (8, 0)
    assert c.right() == (None, 0)
    assert c.up()    == (9, 1)
    assert c.down()  == (9, None)

def test_top_left_corner():
    """ Test that a cell on the top left corner of the grid is correct. """

    # Instantiate a cell on the top left corner of a 10x10 grid.
    c = Cell(0, 9, 10, 10)

    # Make sure that the cell has 2 neighbours.
    assert c.neighbours() == 2

    # Check the coordinates of the neighbours.
    assert c.left()  == (None, 9)
    assert c.right() == (1, 9)
    assert c.up()    == (0, None)
    assert c.down()  == (0, 8)

def test_top_right_corner():
    """ Test that a cell on the top right corner of the grid is correct. """

    # Instantiate a cell on the top right corner of a 10x10 grid.
    c = Cell(9, 9, 10, 10)

    # Make sure that the cell has 2 neighbours.
    assert c.neighbours() == 2

    # Check the coordinates of the neighbours.
    assert c.left()  == (8, 9)
    assert c.right() == (None, 9)
    assert c.up()    == (9, None)
    assert c.down()  == (9, 8)
