import numpy as np
import csv
from numpy import matrix, linalg
import math
import pylab
from pylab import *
import random


datafiles = []
datafiles.append('../data/dataset0.txt')
datafiles.append('../data/dataset1.txt')
datafiles.append('../data/dataset2.txt')
datafiles.append('../data/dataset3.txt')
datafiles.append('../data/dataset4.txt')

##### FINDING CORRELATION COEFFICIENTS #####

N1=1000
bins=20
#zeroes1=array([0.0]*N1)
zeroes1=np.zeros(N1)
zeroes2=array([0.0]*int((N1*.68)))
CorrCoefarray=array([zeroes1]*5)
SD=array([0.0]*5)
range1=array([0.0]*5)


for count,datafile in enumerate(datafiles):

    ############################################################################
    # Read in the data from the data files
    ############################################################################
    infile = open(datafile,'r')       
    lines=infile.readlines()

    N=len(lines)
    data=matrix([[0.0]*2]*N)
    index=0

    for i in range(N):
        content = np.array(lines[i].split()).astype('float')
        data[index,0] = content[0]
        data[index,1] = content[1]
        index=index+1

    ############################################################################
    # Finished reading in the data!
    ############################################################################

    ### Datasets ###

    ave=matrix([[0.0]*2]*1)

    for i in range(N):
        ave[0,0]=ave[0,0]+data[i,0]
        ave[0,1]=ave[0,1]+data[i,1]

    ave=ave/N
    normal=data-ave

    Cov=normal.T*normal

    Corr=matrix([[0.0]*len(Cov)]*len(Cov.T))

    for i in range(len(Cov)):
        for j in range(len(Cov.T)):
            Corr[i,j]=Cov.T[i,j]/sqrt((Cov.T[i,i]*Cov.T[j,j]))


    ##### FINDING UNCERTAINTY #####
            
    ############################################################################
    # Create N1 fake data samples for the bootstrapping.
    ############################################################################
    zeroes=matrix([[0.0]*2]*N)
    newmatrix=matrix([[0.0]*2]*N)
    CorrCoefmatrix=array([0.0]*(N1))
    CorrCoefsorted=array([0.0]*int((N1*.68)))
    matrixarray=array([zeroes]*N1)
    for i in range(N1):
        for j in range(N):
            a=random.randrange(0,N)
            newmatrix[j,0]=data[a,0]
            newmatrix[j,1]=data[a,1]

        matrixarray[i]=newmatrix


    ############################################################################
    # Calculate the corr coeff for *each* boostrap sample.
    ############################################################################
    for i in range(N1):
    
        ave=matrix([[0.0]*2]*1)

        for j in range(N):
            ave[0,0]=ave[0,0]+matrixarray[i][j,0]
            ave[0,1]=ave[0,1]+matrixarray[i][j,1]
    
        ave=ave/N
        normal=matrixarray[i]-ave
    
        Cov=normal.T*normal
    
        Corr1=matrix([[0.0]*len(Cov)]*len(Cov.T))
    
        for k in range(len(Cov)):
            for l in range(len(Cov.T)):
                Corr1[k,l]=Cov.T[k,l]/sqrt((Cov.T[k,k]*Cov.T[l,l]))

            CorrCoefmatrix[i]=Corr1[0,1]


    CorrCoefarray[count]=CorrCoefmatrix
    
    CorrCoefmatrix=sorted(CorrCoefmatrix)
    
    for i in range(len(CorrCoefsorted)):
        CorrCoefsorted[i]=CorrCoefmatrix[i+(int(N1*.16))]
    

    range1[count]=(CorrCoefsorted[len(CorrCoefsorted)-1]-CorrCoefsorted[0])/2
   
        
    
##    ave=0.0
    
##    for i in range(N1):
##
##        ave=ave+CorrCoefarray[count][i]
##
##    
##    ave=ave/N1
##    normal=CorrCoefarray[count]-ave
##    for i in range(N1):
##        
##        SD[count]=SD[count]+normal[i]**2
##
##    SD[count]=math.sqrt(SD[count]/N1)
        

    #figure()
    #pos=np.arange(len(CorrCoefarray[count]))
    #pylab.bar(pos,CorrCoefarray[count])

    

    #print Corr0[0,1]


    figure()
    plot(data[:,0],data[:,1],'+')
    mytitle = "Dataset %d: %3.2f correlation +- %3.3f" % (count, Corr[0,1], range1[count])
    title(mytitle)
    xlabel('x')
    ylabel('y')

    figure()
    hist(CorrCoefmatrix,bins=bins)
    title("Bootstrap histogram for dataset " + str(count))
    xlabel('Correlation Coefficient')
    ylabel('Frequency')


show()


