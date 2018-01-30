#!/usr/bin/env python3
"""
Comparison of three different approaches to perform piecewise (linear) interpolation in Python
    * scipy.interpolate.InterpolatedUnivariateSpline
    * scipy.interp1d
    * numpy.interp
    
All three methods produce identical results for linear interpolation.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline, interp1d

# Define 1D number space
npoints = 10
x = np.linspace(0, 10, npoints)
y = np.exp(-x/3.0)

def scipy_univariatespline(x, y):
    # For linear piecewise interpolation, k = 1
    spl = InterpolatedUnivariateSpline(x, y, k=1)
    xs = np.linspace(0, 10, npoints*10.0)
    plt.plot(x, y, 'o', xs, spl(xs), 'r-')
    plt.savefig('scipy_univariatespline.png')
    plt.close()
    
def scipy_interp1D(x, y):
    spl = interp1d(x, y)
    xs = np.linspace(0, 10, npoints*10.0)
    plt.plot(x, y, 'o', xs, spl(xs), 'g-')
    plt.savefig('scipy_interp1D.png')
    plt.close()
    
def numpy_interp1D(x, y):
    xs = np.linspace(0, 10, npoints*10.0)
    ys = np.interp(xs, x, y)
    plt.plot(x, y, 'o', xs, ys, 'b-')
    plt.savefig('np_interp1D.png')
    plt.close()
    

if __name__ == "__main__":
    
    # InterpolatedUnivariateSpline in scipy (for piecewise, k=1)
    scipy_univariatespline(x, y)
    
    # piecewise linear interpolation in scipy
    scipy_interp1D(x, y)
    
    # piecewise linear interpolation in numpy
    numpy_interp1D(x, y)
    