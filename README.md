# piecewise-interpolation
A comparison of three different ways to perform piecewise (linear) interpolation in Python
 - `scipy.interpolate.InterpolatedUnivariateSpline`
 - `scipy.interpolate.interp1d`
 - `numpy.interp`
 
 `scipy` offers a rich set of wrappers (of well-known FORTRAN libraries) to perform spline interpolation. 
 However, if one just wants to perform linear interpolation, `numpy.interp` works just fine. All three methods produce identical results for linear interpolation. 
