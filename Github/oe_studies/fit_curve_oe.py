import sys
import numpy as np
import matplotlib.pylab as plt
from scipy import optimize


################################################################################
def fitfunc(p, x):
    ret = p[0]*x[0] + p[1]*x[1] + p[2]*x[2] + p[3]*x[3] + p[4]*x[4]
    return ret

################################################################################
def errfunc(p, x, y, yerr):
    ret =  (((fitfunc(p, x)-y)**2)/yerr**2).sum()
    return ret


oe,efgpct,ftr,tor,orr = np.loadtxt('teamStats.dat', dtype=float, usecols=(0,1,2,3,4), unpack=True)
ftp,ftp = np.loadtxt('FTP.dat', dtype=float, usecols=(0,0), unpack=True)

print oe
print efgpct
print ftr
print tor
print orr
print ftp

x = [efgpct,ftr,tor,orr,ftp]
for i,xpt in enumerate(x):
    xlo = min(xpt)
    xhi = max(xpt)
    
    # Rescale between 0 and 1
    xpt = (xpt-xlo)/(xhi-xlo)

    x[i] = xpt
    print x[i]

y = oe

yerr = np.ones(len(y))*0.01

params_starting_vals = [1.0, 1., 1., 1., 1.]
params_final_vals = optimize.fmin(errfunc, params_starting_vals, args=(x,y,yerr))

print params_final_vals 

print params_final_vals/sum(params_final_vals)

