import sys

import scipy

import numpy as np

import matplotlib.pylab as plt

oe,efgpct,ftr,tor,orr = np.loadtxt('teamStats.dat', dtype=float, usecols=(0,1,2,3,4), unpack=True)
ftp,ftp = np.loadtxt('FTP.dat', dtype=float, usecols=(0,0), unpack=True)

print oe

plt.figure()
plt.plot(oe,efgpct,'o')

plt.figure()
plt.plot(oe,ftr,'o')


plt.figure()
plt.plot(oe,tor,'o')


plt.figure()
plt.plot(oe,orr,'o')


plt.figure()
plt.plot(oe,ftp,'o')




plt.figure()
plt.plot(efgpct,ftp,'o')

plt.figure()
plt.plot(efgpct,ftr,'o')






plt.show()
