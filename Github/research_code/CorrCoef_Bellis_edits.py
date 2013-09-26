import numpy as np
import csv
from numpy import matrix, linalg
import math
import pylab
from pylab import *
import glob
import re


datafiles = []
datafiles.append('../data/dataset0.txt')
datafiles.append('../data/dataset1.txt')
datafiles.append('../data/dataset2.txt')
datafiles.append('../data/dataset3.txt')
datafiles.append('../data/dataset4.txt')


for count,datafile in enumerate(datafiles):

    infile = open(datafile,'r')       
    lines=infile.readlines()

    N0=len(lines)
    data0=matrix([[0.0]*2]*N0)
    index=0

    for i in range(N0):
        content = np.array(lines[i].split()).astype('float')
        data0[index,0] = content[0]
        data0[index,1] = content[1]
        index=index+1

    ### Dataset0 ###

    ave0=matrix([[0.0]*2]*1)

    for i in range(N0):
        ave0[0,0]=ave0[0,0]+data0[i,0]
        ave0[0,1]=ave0[0,1]+data0[i,1]

    ave0=ave0/N0
    normal0=data0-ave0

    Cov0=normal0.T*normal0

    Corr0=matrix([[0.0]*len(Cov0)]*len(Cov0.T))

    for i in range(len(Cov0)):
        for j in range(len(Cov0.T)):
            Corr0[i,j]=Cov0.T[i,j]/sqrt((Cov0.T[i,i]*Cov0.T[j,j]))

    print Corr0[0,1]

    figure()
    plot(data0[:,0],data0[:,1],'+')
    mytitle = "Dataset %d: %3.2f correlation" % (count, Corr0[0,1])
    title(mytitle)
    xlabel('x')
    ylabel('y')
        


show()


