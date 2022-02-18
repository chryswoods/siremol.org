#cython: language_level=3

import numpy as np
import os
import csv
import urllib.request


def load_and_parse_data(percent=100):
    """This function downloads, parses and returns the data

       percent: float
           The percentage of data to load. Load less data if
           processing is too slow

       Returns
       =======

       (ids,       : list of IDs of the different patterns - one pattern per row
        varieties, : list of the varieties that can be distinguished - one per column
        data)      : 2D numpy array of integers, -1, 0, 1, 2, which show whether
                     or not this pattern can distinguish the variety
    """
    filename = "AppleGenotypes.csv"

    if not os.path.exists(filename):
        # The file does not exist - download it!
        url = "https://raw.githubusercontent.com/chryswoods/minimalmarkers/main/example"
        filename = "AppleGenotypes.csv"

        urllib.request.urlretrieve(f"{url}/{filename}", filename)

    # Now parse the data. This reads the data using the
    # csv module, doing some formatting that is needed
    # for this type of data
    lines = open(filename, "r").readlines()

    # try to discover the separator used for the file (should be a comma)
    dialect = csv.Sniffer().sniff(lines[0], delimiters=[" ", ",", "\t"])

    # the varieties are the column headers (minus the first column
    # which is the ID code for the pattern)
    varieties = []

    for variety in list(csv.reader([lines[0]], dialect=dialect))[0][1:]:
        varieties.append(variety.lstrip().rstrip())

    ids = []
    nrows = len(lines) - 1
    ncols = len(varieties)

    if percent != 100:
        nrows = min(nrows, int(nrows * percent / 100.0))

    data = np.full((nrows, ncols), -1, np.int8)

    npatterns = 0

    irow = np.full(ncols, -1, np.int8)

    for i in range(1, nrows+1):
        parts = list(csv.reader([lines[i]], dialect=dialect))[0]

        if len(parts) != ncols+1:
            print("WARNING - invalid row! "
                  f"'{parts}' : {len(parts)} vs {ncols}")
        else:
            ids.append(parts[0])
            row = np.asarray(parts[1:], np.string_)
            pattern = data[npatterns]
            pattern[(row == b'0') | (row == b'A')] = 0
            pattern[(row == b'1') | (row == b'AB')] = 1
            pattern[(row == b'2') | (row == b'B')] = 2

            npatterns += 1

    # Verify that the data has the right dimensions
    nrows = len(ids)
    ncols = len(varieties)

    assert nrows == data.shape[0]
    assert ncols == data.shape[1]

    return (ids, varieties, data)


##############
############## We will be speeding up the code below
##############

def calculate_scores(data):
    """Calculate the score for each row. This is calculated
       as the sum of pairs of values on each row where the values
       are not equal to each other, and neither are equal to -1.

       Returns
       =======

            scores : numpy array containing the scores
    """
    nrows = data.shape[0]
    ncols = data.shape[1]

    # Here is the list of scores
    scores = np.zeros(nrows)

    # Loop over all rows
    for irow in range(0, nrows):
        for i in range(0, ncols):
            for j in range(i, ncols):
                ival = data[irow, i]
                jval = data[irow, j]

                if ival != -1 and jval != -1 and ival != jval:
                    scores[irow] += 1

    return scores


def get_index_of_best_score(scores):
    """Return the index of the best score from the passed list of scores"""

    # Now find the pattern with the highest score
    best_score = 0
    best_pattern = None

    for irow in range(0, len(scores)):
        if scores[irow] > best_score:
            best_pattern = irow
            best_score = scores[irow]

    return best_pattern
