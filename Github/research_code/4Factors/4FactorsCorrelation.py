
import glob
import numpy as np
from numpy import matrix, linalg

a=glob.glob('/Users/DanLo1108/Documents/AdvancedLab/Data Files/teamStats.txt')
b=str(a[0])
infile=open(b,'r')
lines=infile.readlines()

OE=matrix([[0.0]*1]*30)         #Offensive Efficiency (Pts/100 poss)
eFG=matrix([[0.0]*1]*30)        #Effective FG percentage (weighted for 3 pointers)
FTR=matrix([[0.0]*1]*30)        #FTA/FGA
TOR=matrix([[0.0]*1]*30)        #% of possessions ended in TO
ORR=matrix([[0.0]*1]*30)        #% of Offensive rebounds grabbed

startData=0
endData=30

index=0

N=len(lines)


for i in range(N):
    if((i >= startData) and (i < endData)):
        content=np.array(lines[i].split()).astype('float')
        OE[index,0]=content[0]
        eFG[index,0]=content[1]/100
        FTR[index,0]=content[2]/100
        TOR[index,0]=content[3]/100
        ORR[index,0]=content[4]/100
        index=index+1


a=glob.glob('/Users/DanLo1108/Documents/AdvancedLab/Data Files/FTP.txt')
b=str(a[0])
infile=open(b,'r')
lines=infile.readlines()

FTP=matrix([[0.0]*1]*30)        #Free throw percentage

startData=0
endData=30

index=0

N=len(lines)

for i in range(N):
    if((i >= startData) and (i < endData)):
        content=np.array(lines[i].split()).astype('float')
        FTP[index,0]=content[0]/100
        index=index+1

FTpFGA=matrix([[0.0]*1]*30)     #FTM/FGA

for i in range(30):
    FTpFGA[i]=FTR[i]*FTP[i]



import CorrelationCoefficient
from CorrelationCoefficient import corr_coef

global CorrelationCoef

eFGcorr=corr_coef(eFG[:,0],OE[:,0])  #Correlation between eFG% and OE
FTRcorr=corr_coef(FTR[:,0],OE[:,0])  #Correlation between FTR and OE
TORcorr=corr_coef(TOR[:,0],OE[:,0])  #Correlation between TOR and OE
ORRcorr=corr_coef(ORR[:,0],OE[:,0])  #Correlation between ORR and OE
FTPcorr=corr_coef(FTP[:,0],OE[:,0])  #Correlation between FTP and OE
FTpFGAcorr=corr_coef(FTpFGA[:,0],OE[:,0])


import Bootstrap
from Bootstrap import bootstrap

eFGuc=bootstrap(eFG[:,0],OE[:,0])
FTRuc=bootstrap(FTR[:,0],OE[:,0])
TORuc=bootstrap(TOR[:,0],OE[:,0])
ORRuc=bootstrap(ORR[:,0],OE[:,0])
FTPuc=bootstrap(FTP[:,0],OE[:,0])
FTpFGAuc=bootstrap(FTpFGA[:,0],OE[:,0])


