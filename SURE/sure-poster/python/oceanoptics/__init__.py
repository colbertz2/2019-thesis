# oceanoptics module

import numpy as np
import os.path as path
import sys


def getdata(filename):
    """
    Import spectral data from an Ocean Optics/Overture CSV export.

    Parameters:
    -------------
    **filename:** *String* Imports a file from this path. File must be type CSV, fit the format of data exported from Overture software.

    Returns:
    -------------
    **x, y:** *Tuple* Returns arrays containing the first and second columns of data, respectively.
    """

    # Resolve the absolute path of the file
    filepath = path.abspath(filename)

    # Check the file type
    filext = path.splitext(filepath)
    assert filext[1] == '.csv'

    # Import data using numpy
    data = np.genfromtxt(filepath, delimiter=',')

    # Pull the data into separate arrays
    x = data[:,0]
    y = data[:,1]

    return x, y

if __name__ == "__main__":
    print getdata(sys.argv[1])