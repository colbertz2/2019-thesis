# test_OceanOptics.py

import oceanoptics
import os.path as path
import numpy as np

# Test CSV file
testcsv = path.join(path.dirname(__file__), 'test.csv')

# Make sure file has good test data
testdata = np.asarray([
    [0, 0],
    [1, 2],
    [2, 4],
    [3, 6],
    [4, 8],
    [5, 10]
])
np.savetxt(testcsv, testdata, delimiter=',')


def test_oceanoptics():
    # Get data from test file
    x, y = oceanoptics.getdata(testcsv)

    # What does it look like?
    for i in range(0, len(x)):
        assert y[i] == 2 * x[i]