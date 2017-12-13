from ..grid import Cell

def test_bulk():
    """ Test that a cell in the bulk of the grid is correct. """

    # Instantiate a cell in the bulk of a 4x4 grid.
    c = Cell(2, 2, 4, 4)

    # Make sure that the cell has 4 neighbours.
    assert c.neighbours() == 4

    # Check the coordinates of the neighbours.
    assert c.left()  == (1, 2)
    assert c.right() == (3, 2)
    assert c.up()    == (2, 3)
    assert c.down()  == (2, 1)

def test_left_edge():
    """ Test that a cell on the left edge of the grid is correct. """

    # Instantiate a cell on the left edge of a 4x4 grid.
    c = Cell(0, 2, 4, 4)

    # Make sure that the cell has 3 neighbours.
    assert c.neighbours() == 3

    # Check the coordinates of the neighbours.
    assert c.left()  == None
    assert c.right() == (1, 2)
    assert c.up()    == (0, 3)
    assert c.down()  == (0, 1)

def test_right_edge():
    """ Test that a cell on the right edge of the grid is correct. """

    # Instantiate a cell on the right edge of a 4x4 grid.
    c = Cell(3, 2, 4, 4)

    # Make sure that the cell has 3 neighbours.
    assert c.neighbours() == 3

    # Check the coordinates of the neighbours.
    assert c.left()  == (2, 2)
    assert c.right() == None
    assert c.up()    == (3, 3)
    assert c.down()  == (3, 1)

def test_bottom_edge():
    """ Test that a cell on the bottom edge of the grid is correct. """

    # Instantiate a cell on the bottom edge of a 4x4 grid.
    c = Cell(2, 0, 4, 4)

    # Make sure that the cell has 3 neighbours.
    assert c.neighbours() == 3

    # Check the coordinates of the neighbours.
    assert c.left()  == (1, 0)
    assert c.right() == (3, 0)
    assert c.up()    == (2, 1)
    assert c.down()  == None

def test_top_edge():
    """ Test that a cell on the top edge of the grid is correct. """

    # Instantiate a cell on the top edge of a 4x4 grid.
    c = Cell(2, 3, 4, 4)

    # Make sure that the cell has 3 neighbours.
    assert c.neighbours() == 3

    # Check the coordinates of the neighbours.
    assert c.left()  == (1, 3)
    assert c.right() == (3, 3)
    assert c.up()    == None
    assert c.down()  == (2, 2)

def test_bottom_left_corner():
    """ Test that a cell on the bottom left corner of the grid is correct. """

    # Instantiate a cell at the bottom left corner of a 4x4 grid.
    c = Cell(0, 0, 4, 4)

    # Make sure that the cell has 2 neighbours.
    assert c.neighbours() == 2

    # Check the coordinates of the neighbours.
    assert c.left()  == None
    assert c.right() == (1, 0)
    assert c.up()    == (0, 1)
    assert c.down()  == None

def test_bottom_right_corner():
    """ Test that a cell at the bottom right corner of the grid is correct. """

    # Instantiate a cell on the bottom right corner of a 4x4 grid.
    c = Cell(3, 0, 4, 4)

    # Make sure that the cell has 2 neighbours.
    assert c.neighbours() == 2

    # Check the coordinates of the neighbours.
    assert c.left()  == (2, 0)
    assert c.right() == None
    assert c.up()    == (3, 1)
    assert c.down()  == None

def test_top_left_corner():
    """ Test that a cell on the top left corner of the grid is correct. """

    # Instantiate a cell on the top left corner of a 4x4 grid.
    c = Cell(0, 3, 4, 4)

    # Make sure that the cell has 2 neighbours.
    assert c.neighbours() == 2

    # Check the coordinates of the neighbours.
    assert c.left()  == None
    assert c.right() == (1, 3)
    assert c.up()    == None
    assert c.down()  == (0, 2)

def test_top_right_corner():
    """ Test that a cell on the top right corner of the grid is correct. """

    # Instantiate a cell at the top right corner of a 4x4 grid.
    c = Cell(3, 3, 4, 4)

    # Make sure that the cell has 2 neighbours.
    assert c.neighbours() == 2

    # Check the coordinates of the neighbours.
    assert c.left()  == (2, 3)
    assert c.right() == None
    assert c.up()    == None
    assert c.down()  == (3, 2)
