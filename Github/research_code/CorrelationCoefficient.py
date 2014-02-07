import numpy as np
from numpy import linalg, matrix, array
import math

#####################################################
#     ####Defining Correlation Coefficient####      #
#####################################################

global CorrelationCorf

def corr_coef(data1,data2):

    M=len(data1)
    N1=1000
       
    CorrCoef1=matrix([[0.0]*1]*N1)
  
    normal=matrix([[0.0]*2]*len(data1))       #normalized pass/win pct data

    ave=matrix([[0.0]*2]*1)             #finding the mean of each dataset

    for i in range(len(normal)):
        ave[0,0]=ave[0,0]+data1[i]
        ave[0,1]=ave[0,1]+data2[i]

    ave=ave/M
    for i in range(M):
        normal[i,0]=data1[i]-ave[0,0]
        normal[i,1]=data2[i]-ave[0,1]

    Cov=normal.T*normal                          #Covariance matrix of 2 data sets

 
    Corr=matrix([[0.0]*len(Cov)]*len(Cov.T))      #Correlation matrix of 2 data sets


    for i in range(len(Cov)):
        for j in range(len(Cov.T)):
            Corr[i,j]=Cov.T[i,j]/math.sqrt((Cov.T[i,i]*Cov.T[j,j]))

    #global CorrCoef1
    CorrCoef1[0]=Corr[0,1]

    global CorrelationCoef
    CorrelationCoef=CorrCoef1[0]

    return CorrelationCoef
