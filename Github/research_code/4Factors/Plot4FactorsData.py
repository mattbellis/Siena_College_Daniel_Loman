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




import CorrelationCoefficient
from CorrelationCoefficient import corr_coef

global CorrelationCoef

eFG_OEcorr=corr_coef(eFG[:,0],OE[:,0])
FTR_OEcorr=corr_coef(FTR[:,0],OE[:,0])
TOR_OEcorr=corr_coef(TOR[:,0],OE[:,0])
ORR_OEcorr=corr_coef(ORR[:,0],OE[:,0])
FTR_eFGcorr=corr_coef(FTR[:,0],eFG[:,0])
TOR_eFGcorr=corr_coef(TOR[:,0],eFG[:,0])
ORR_eFGcorr=corr_coef(ORR[:,0],eFG[:,0])
TOR_FTRcorr=corr_coef(TOR[:,0],FTR[:,0])
ORR_FTRcorr=corr_coef(ORR[:,0],FTR[:,0])
ORR_TORcorr=corr_coef(ORR[:,0],TOR[:,0])

import Bootstrap
from Bootstrap import bootstrap

eFG_OEbs=bootstrap(eFG[:,0],OE[:,0])
FTR_OEbs=bootstrap(FTR[:,0],OE[:,0])
TOR_OEbs=bootstrap(TOR[:,0],OE[:,0])
ORR_OEbs=bootstrap(ORR[:,0],OE[:,0])
FTR_eFGbs=bootstrap(FTR[:,0],eFG[:,0])
TOR_eFGbs=bootstrap(TOR[:,0],eFG[:,0])
ORR_eFGbs=bootstrap(ORR[:,0],eFG[:,0])
TOR_FTRbs=bootstrap(TOR[:,0],FTR[:,0])
ORR_FTRbs=bootstrap(ORR[:,0],FTR[:,0])
ORR_TORbs=bootstrap(ORR[:,0],TOR[:,0])


figure()
subplot(2,2,1)

plot(eFG,OE,'*')
title("correlation = " + str(eFG_OEcorr) + " +- " + str(eFG_OEbs),fontsize=14)
xlabel("Effective Field Goal Percentage")
ylabel("Offensive Efficiency")

subplot(2,2,2)

plot(FTR,OE,'*')
title("correlation = " + str(FTR_OEcorr) + " +- " + str(FTR_OEbs),fontsize=14)
xlabel("Free Throw Rate")
ylabel("Offensive Efficiency")

subplot(2,2,3)

plot(TOR,OE,'*')
title("correlation = " + str(TOR_OEcorr) + " +- " + str(TOR_OEbs),fontsize=14)
xlabel("Turnover Rate")
ylabel("Offensive Efficiency")

subplot(2,2,4)

plot(ORR,OE,'*')
title("correlation = " + str(ORR_OEcorr) + " +- " + str(ORR_OEbs),fontsize=14)
xlabel("Offensive Rebound Rate")
ylabel("Offensive Efficiency")

figure()
       
subplot(3,2,1)

plot(FTR,eFG,'*')
title("correlation = " + str(FTR_eFGcorr) + " +- " + str(FTR_eFGbs),fontsize=14)
xlabel("Free Throw Rate")
ylabel("Effective Field Goal Percentage")

subplot(3,2,2)

plot(TOR,eFG,'*')
title("correlation = " + str(TOR_eFGcorr) + " +- " + str(TOR_eFGbs),fontsize=14)
xlabel("Turnover Rate")
ylabel("Effective Field Goal Percentage")

subplot(3,2,3)

plot(ORR,eFG,'*')
title("correlation = " + str(ORR_eFGcorr) + " +- " + str(ORR_eFGbs),fontsize=14)
xlabel("Offensive Rebound Rate")
ylabel("Effective Field Goal Percentage")

subplot(3,2,4)

plot(TOR,FTR,'*')
title("correlation = " + str(TOR_FTRcorr) + " +- " + str(FTR_eFGbs),fontsize=14)
xlabel("Turnover Rate")
ylabel("Free Throw Rate")

subplot(3,2,5)

plot(ORR,FTR,'*')
title("correlation = " + str(ORR_FTRcorr) + " +- " + str(ORR_eFGbs),fontsize=14)
xlabel("Offensive Rebound Rate")
ylabel("Free Throw Rate")


subplot(3,2,6)

plot(ORR,TOR,'*')
title("correlation = " + str(ORR_TORcorr) + " +- " + str(ORR_TORbs),fontsize=14)
xlabel("Offensive Rebound Rate")
ylabel("Turnover Rate")

       
show()






