# spectra module

import numpy as np

def averagespectra(data):
    """
    Takes a tuple of arrays containing spectral data, and averages them together.
    """

    # Arrays must be the same length
    for i in data:
        assert len(i) == len(data[0])

    avgdata = np.zeros(len(data[0]))
    for i in data:
        avgdata += i

    avgdata = avgdata / len(data)

    return avgdata

def normalizespectra(data):
    """
    Takes a tuple of arrays containing spectral data, and normalizes them relatively to 1.
    """

    mm = 0.
    for i in data:
        m = np.max(i)
        if (m > mm): mm = m

    data /= mm

    return data

def backgroundcorrect(reference, data):
    """
    Subtracts background reference data from actual data and returns the result.

    Parameters:
    ---------------
    **reference:** *Array-like* Background reference data
    **data:** *Array-like* Tuple of arrays of data to subtract from

    Returns:
    ---------------
    **data**: *Array-like* Tuple of arrays of corrected data
    """

    # Arrays must be the same length
    for i in data:
        assert len(i) == len(reference)

    reference = np.array(reference)
    data = np.array(data)

    data -= reference

    return data

if __name__ == "__main__":
    a = [0.,1.,2.,3.,4.,5.]
    b = [0.,2.,4.,6.,8.,10.]
    c = [0.,3.,6.,9.,12.,15.]
    # print averagespectra((a, b, c))
    # print normalizespectra((a,b,c))
    print backgroundcorrect(a, (b, c))