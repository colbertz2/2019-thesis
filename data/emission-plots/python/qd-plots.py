# qd-plots.py

import numpy as np
import matplotlib.pyplot as plt
import os.path as path
import fluorimeter as fl
import oceanoptics as oo
import spectra as sp
import scipy.signal as sig

## OCEAN OPTICS DATA ##

# Get data from original sources
oceanfiles = [
    'QD-A-1.csv',
    'QD-A-2.csv',
    'QD-A-3.csv',
    'QD-B-1.csv',
    'QD-B-2.csv',
    'QD-B-3.csv',
    'QD-Bkg.csv',
    'QD-Dark.csv']

# Declare data container for later
oceandata = []
oceanwavelength = []

# Declare path to OO data
oceandir = path.abspath("../data/oceanoptics/qd")

# Setup the oceandata container using the first file
w, d = oo.getdata(path.abspath(path.join(oceandir, oceanfiles[0])))
oceanwavelength = w
oceandata.append(d)

# For each of the input files
for fn in oceanfiles[1:]:
    # Resolve path to file
    fn = path.abspath(path.join(oceandir, fn))
    
    # Get data
    w, d = oo.getdata(fn)

    # Add data into new column in oceandata
    oceandata.append(d)

# Finally, convert oceandata and oceanwavelength to numpy arrays
oceandata = np.array(oceandata)
oceanwavelength = np.array(oceanwavelength)

# Average data by ROI (A, B)
oceanbyroi = np.array([sp.averagespectra(oceandata[0:3]), sp.averagespectra(oceandata[3:6])])

# Background correct averaged oceandata
oceanbkg = oceandata[6]
oceanbyroi_c = sp.backgroundcorrect(oceanbkg, oceanbyroi)

# Normalize ocean optics data
oceanbyroi_cnorm = sp.normalizespectra(oceanbyroi_c)



## FLUOROLOG DATA ##

# File names
fldatafile = path.abspath("../data/fluorimeter/qd/Data.csv")
flbackgroundfile = path.abspath("../data/fluorimeter/qd/Background.csv")

# Read data in
fldataheaders_raw, fldata_raw = fl.readfile(fldatafile)
flbkgheaders_raw, flbkg_raw = fl.readfile(flbackgroundfile)

# Segregate wavelength from actual data
flwavelength = fl.getwavelength(fldataheaders_raw, fldata_raw)
fldataheaders, fldata = fl.getdata(fldataheaders_raw, fldata_raw)
flbkgheaders, flbkg = fl.getdata(flbkgheaders_raw, flbkg_raw)

# Select which fluoro data to actually use
flindex = 1     # S1c / R1c

# Transpose data because it's in columns
fldata = np.transpose(fldata)
flbkg = np.transpose(flbkg)

# Background correct
fldata_c = sp.backgroundcorrect(flbkg[flindex], fldata)

# Normalize
fldata_cnorm = sp.normalizespectra(fldata_c)

## OTHER ANALYSIS ##

# Using SciPy signal.find_peaks
# pk = sig.find_peaks(oceanbyroi_cnorm[0])
# print len(pk[0])
# print pk[0]

## PLOTS ##

# Init plot
plt.figure()
# plt.title("CdSe Quantum Dots Emission Spectrum (405nm excitation)")
plt.xlabel("Emission Wavelength (nm)")
plt.ylabel("PL Intensity (arb. units)")

# Ocean optics
plt.plot(oceanwavelength, oceanbyroi_cnorm[0], label="New System") # ROI A
# plt.plot(oceanwavelength, oceanbyroi_cnorm[1], label="New System (ROI B)")

# Fluorolog
plt.plot(flwavelength, fldata_cnorm[flindex], '-', label="Existing System") # ROI A

# Other plot features
plt.legend(loc='best')
plt.tight_layout()
plt.xlim(500, 650)
plt.ylim(-0.1, 1.1)

plt.show()