import random
import glob
import numpy as np
from numpy import matrix, linalg
import matplotlib
import pylab
from pylab import *

#############################
###    IMPORTING DATA     ###
#############################

a=glob.glob('/Users/DanLo1108/Documents/AdvancedLab/Data Files/teamStats.txt')
b=str(a[0])
infile=open(b,'r')
lines=infile.readlines()

OE=matrix([[0.0]*1]*210)
eFG=matrix([[0.0]*1]*210)
FTR1=matrix([[0.0]*1]*210)
TOR=matrix([[0.0]*1]*210)
ORR=matrix([[0.0]*1]*210)

startData=0
endData=210

index=0

N=len(lines)

for i in range(N):
    if((i >= startData) and (i < endData)):
        content=np.array(lines[i].split()).astype('float')
        OE[index,0]=content[0]
        eFG[index,0]=content[1]/100
        FTR1[index,0]=content[2]/100
        TOR[index,0]=content[3]/100
        ORR[index,0]=content[4]/100
        index=index+1


a=glob.glob('/Users/DanLo1108/Documents/AdvancedLab/Data Files/FTP.txt')
b=str(a[0])
infile=open(b,'r')
lines=infile.readlines()

FTP=matrix([[0.0]*1]*210)

startData=0
endData=210

index=0

N=len(lines)

for i in range(N):
    if((i >= startData) and (i < endData)):
        content=np.array(lines[i].split()).astype('float')
        FTP[index,0]=content[0]/100
        index=index+1

FTR=matrix([[0.0]*1]*210)

for i in range(210):
    FTR[i]=FTR1[i]*FTP[i]


##########################################################################
### k-nearest neighbor algorithm

## Get data ##

print(__doc__)

from sklearn.cluster import MeanShift, estimate_bandwidth
from sklearn.datasets.samples_generator import make_blobs


percent=.20

good_bad="good"

Y=matrix([[0.0]*5]*210)

for i in range(len(Y)):

    Y[i,0]=OE[i]
    Y[i,1]=eFG[i]
    Y[i,2]=FTR[i]
    Y[i,3]=TOR[i]
    Y[i,4]=ORR[i]

Y=array(Y)
Y1=sorted(Y, key=lambda Y_entry: Y_entry[0])

X=matrix([[0.0]*4]*int(210*percent))

if(good_bad=="good"):
    
    for i in range(len(X)):
        X[i,0]=Y1[209-i][1]
        X[i,1]=Y1[209-i][2]
        X[i,2]=Y1[209-i][3]
        X[i,3]=Y1[209-i][4]

if(good_bad=="bad"):
    
    for i in range(len(X)):
        X[i,0]=Y1[i][1]
        X[i,1]=Y1[i][2]
        X[i,2]=Y1[i][3]
        X[i,3]=Y1[i][4]
    

_=np.array([0.0]*len(X))

X=array(X)



###############################################################################
# Compute clustering with MeanShift

# The following bandwidth can be automatically detected using
bandwidth = estimate_bandwidth(X, quantile=0.2, n_samples=500)

ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
ms.fit(X)
labels = ms.labels_
cluster_centers = ms.cluster_centers_

labels_unique = np.unique(labels)
n_clusters_ = len(labels_unique)

print("number of estimated clusters : %d" % n_clusters_)




print("cluster centers : ")
print cluster_centers




