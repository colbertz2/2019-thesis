# fluorimeter module

import numpy as np
import os.path as path
import sys


def readfile(filename):
    """
    Import spectral data from a Horiba Fluorolog CSV file.

    Parameters:
    --------------
    **filename:** *String* Imports a file from this path. File must be type CSV, and fit the format of an Origin worksheet copied to CSV file.

    Returns:
    -------------
    **headers, data:** *Arrays* Containing headers on data and raw data."""

    # Resolve absolute path to the file
    filepath = path.abspath(filename)

    # Check the filetype
    filext = path.splitext(filepath)
    assert filext[1] == '.csv'

    # Import data headers
    headers = np.loadtxt(filepath, delimiter=',', dtype='string')
    headers = headers[0:1]

    # Import data
    data = np.genfromtxt(filepath, delimiter=',', skip_header=2)

    return headers, data

def getwavelength(headers, data):
    """
    From coupled header and data arrays, find a column labelled "Wavelength" and return only that column.
    """

    # Sort data into arrays
    iw = np.where(headers == "Wavelength")
    wavelength = data[:,iw[1][0]]

    return wavelength

def getdata(headers, data):
    """
    From coupled header and data arrays, find columns not labelled "Wavelength" and return them in a 2D array.

    Returns:
    --------------
    **headers, data**
    """

    # Find significant columns
    isig = []
    for j in range(0, len(headers[0])):
        if (headers[0][j] != "Wavelength"):
            isig += [j]

    # Prune original arrays
    headers = headers[:,isig]
    data = data[:,isig]

    return headers, data

if __name__ == "__main__":
    headers, data = readfile(sys.argv[1])
    wavelength = getwavelength(headers, data)
    headers, data = getdata(headers, data)

    print wavelength
    print headers
    print data