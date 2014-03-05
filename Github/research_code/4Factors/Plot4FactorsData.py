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


Y=matrix([[0.0]*5]*210)

for i in range(len(Y)):

    Y[i,0]=OE[i]
    Y[i,1]=eFG[i]
    Y[i,2]=FTR[i]
    Y[i,3]=TOR[i]
    Y[i,4]=ORR[i]

Y=array(Y)
Y1=sorted(Y, key=lambda Y_entry: Y_entry[0])

top50=matrix([[0.0]*5]*105)
bottom50=matrix([[0.0]*5]*105)

for i in range(len(top50)):

        top50[i,0]=Y1[209-i][0]
        top50[i,1]=Y1[209-i][1]
        top50[i,2]=Y1[209-i][2]
        top50[i,3]=Y1[209-i][3]
        top50[i,4]=Y1[209-i][4]

        bottom50[i,0]=Y1[i][0]
        bottom50[i,1]=Y1[i][1]
        bottom50[i,2]=Y1[i][2]
        bottom50[i,3]=Y1[i][3]
        bottom50[i,4]=Y1[i][4]


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

##eFG_OEbs=bootstrap(eFG[:,0],OE[:,0])
##FTR_OEbs=bootstrap(FTR[:,0],OE[:,0])
##TOR_OEbs=bootstrap(TOR[:,0],OE[:,0])
##ORR_OEbs=bootstrap(ORR[:,0],OE[:,0])
##FTR_eFGbs=bootstrap(FTR[:,0],eFG[:,0])
##TOR_eFGbs=bootstrap(TOR[:,0],eFG[:,0])
##ORR_eFGbs=bootstrap(ORR[:,0],eFG[:,0])
##TOR_FTRbs=bootstrap(TOR[:,0],FTR[:,0])
##ORR_FTRbs=bootstrap(ORR[:,0],FTR[:,0])
##ORR_TORbs=bootstrap(ORR[:,0],TOR[:,0])



################################################################
##### Offensive Efficiency on Y axis

figure()
subplot(2,2,1)

plot(eFG,OE,'*')
title("all: correlation = " + str(eFG_OEcorr),fontsize=14)
xlabel("Effective Field Goal Percentage")
ylabel("Offensive Efficiency")

subplot(2,2,2)

plot(FTR,OE,'*')
title("all: correlation = " + str(FTR_OEcorr),fontsize=14)
xlabel("Free Throw Rate")
ylabel("Offensive Efficiency")

subplot(2,2,3)

plot(TOR,OE,'*')
title("all: correlation = " + str(TOR_OEcorr),fontsize=14)
xlabel("Turnover Rate")
ylabel("Offensive Efficiency")

subplot(2,2,4)

plot(ORR,OE,'*')
title("all: corr= " + str(ORR_OEcorr),fontsize=14)
xlabel("Offensive Rebound Rate")
ylabel("Offensive Efficiency")

### top 50 ###

figure()

subplot(2,2,1)

plot(top50[:,1],top50[:,0],'*')
title("best: corr = " + str(corr_coef(top50[:,1],top50[:,0])),fontsize=14)
xlabel("Effective Field Goal Percentage")
ylabel("Offensive Efficiency")

subplot(2,2,2)

plot(top50[:,2],top50[:,0],'*')
title("best: corr = " + str(corr_coef(top50[:,2],top50[:,0])),fontsize=14)
xlabel("Free Throw Rate")
ylabel("Offensive Efficiency")

subplot(2,2,3)

plot(top50[:,3],top50[:,0],'*')
title("best: corr = " + str(corr_coef(top50[:,3],top50[:,0])),fontsize=14)
xlabel("Turnover Rate")
ylabel("Offensive Efficiency")

subplot(2,2,4)

plot(top50[:,4],top50[:,0],'*')
title("best: corr = " + str(corr_coef(top50[:,4],top50[:,0])),fontsize=14)
xlabel("Offensive Rebound Rate")
ylabel("Offensive Efficiency")

### bottom 50 ###

figure()

subplot(2,2,1)

plot(bottom50[:,1],bottom50[:,0],'*')
title("worst: corr = " + str(corr_coef(bottom50[:,1],bottom50[:,0])),fontsize=14)
xlabel("Effective Field Goal Percentage")
ylabel("Offensive Efficiency")

subplot(2,2,2)

plot(bottom50[:,2],bottom50[:,0],'*')
title("worst: corr = " + str(corr_coef(bottom50[:,2],bottom50[:,0])),fontsize=14)
xlabel("Free Throw Rate")
ylabel("Offensive Efficiency")

subplot(2,2,3)

plot(bottom50[:,3],bottom50[:,0],'*')
title("worst: corr = " + str(corr_coef(bottom50[:,3],bottom50[:,0])),fontsize=14)
xlabel("Turnover Rate")
ylabel("Offensive Efficiency")

subplot(2,2,4)

plot(bottom50[:,4],bottom50[:,0],'*')
title("worst: corr = " + str(corr_coef(bottom50[:,4],bottom50[:,0])),fontsize=14)
xlabel("Offensive Rebound Rate")
ylabel("Offensive Efficiency")


############################################################
##### eFG on Y axis

      
figure()
       
subplot(2,2,1)

plot(FTR,eFG,'*')
title("all: corr = " + str(FTR_eFGcorr),fontsize=14)
xlabel("Free Throw Rate")
ylabel("Effective Field Goal Percentage")

subplot(2,2,2)

plot(TOR,eFG,'*')
title("all: corr = " + str(TOR_eFGcorr),fontsize=14)
xlabel("Turnover Rate")
ylabel("Effective Field Goal Percentage")

subplot(2,2,3)

plot(ORR,eFG,'*')
title("all: corr = " + str(ORR_eFGcorr),fontsize=14)
xlabel("Offensive Rebound Rate")
ylabel("Effective Field Goal Percentage")

### top 50 ###

figure()

subplot(2,2,1)

plot(top50[:,2],top50[:,1],'*')
title("best: corr = " + str(corr_coef(top50[:,2],top50[:,1])),fontsize=14)
xlabel("Free Throw Rate")
ylabel("Effective Field Goal Percentage")

subplot(2,2,2)

plot(top50[:,3],top50[:,1],'*')
title("best: corr = " + str(corr_coef(top50[:,3],top50[:,1])),fontsize=14)
xlabel("Turnover Rate")
ylabel("Effective Field Goal Percentage")

subplot(2,2,3)

plot(top50[:,4],top50[:,1],'*')
title("best: corr = " + str(corr_coef(top50[:,4],top50[:,1])),fontsize=14)
xlabel("Offensive Rebound Rate")
ylabel("Effective Field Goal Percentage")

### bottom 50 ###

figure()

subplot(2,2,1)

plot(bottom50[:,2],bottom50[:,1],'*')
title("worst: corr = " + str(corr_coef(bottom50[:,2],bottom50[:,1])),fontsize=14)
xlabel("Free Throw Rate")
ylabel("Effective Field Goal Percentage")

subplot(2,2,2)

plot(bottom50[:,3],bottom50[:,1],'*')
title("worst: corr = " + str(corr_coef(bottom50[:,3],bottom50[:,1])),fontsize=14)
xlabel("Turnover Rate")
ylabel("Effective Field Goal Percentage")

subplot(2,2,3)

plot(bottom50[:,4],bottom50[:,1],'*')
title("worst: corr = " + str(corr_coef(bottom50[:,4],bottom50[:,1])),fontsize=14)
xlabel("Offensive Rebound Rate")
ylabel("Effective Field Goal Percentage")

#########################################################
##### FTR and TOR on Y axis

figure()

subplot(2,2,1)

plot(TOR,FTR,'*')
title("all: corr = " + str(TOR_FTRcorr),fontsize=14)
xlabel("Turnover Rate")
ylabel("Free Throw Rate")

subplot(2,2,2)

plot(ORR,FTR,'*')
title("all: corr = " + str(ORR_FTRcorr),fontsize=14)
xlabel("Offensive Rebound Rate")
ylabel("Free Throw Rate")


subplot(2,2,3)

plot(ORR,TOR,'*')
title("all: corr = " + str(ORR_TORcorr),fontsize=14)
xlabel("Offensive Rebound Rate")
ylabel("Turnover Rate")

### top 50

figure()

subplot(2,2,1)

plot(top50[:,3],top50[:,2],'*')
title("best: corr = " + str(corr_coef(top50[:,3],top50[:,2])),fontsize=14)
xlabel("Turnover Rate")
ylabel("Free Throw Rate")

subplot(2,2,2)

plot(top50[:,4],top50[:,2],'*')
title("best: corr = " + str(corr_coef(top50[:,4],top50[:,2])),fontsize=14)
xlabel("Offensive Rebound Rate")
ylabel("Free Throw Rate")

subplot(2,2,3)

plot(top50[:,4],top50[:,3],'*')
title("best: corr = " + str(corr_coef(top50[:,4],top50[:,3])),fontsize=14)
xlabel("Offensive Rebound Rate")
ylabel("Turnover Rate")


### bottom 50 ###

figure()

subplot(2,2,1)

plot(bottom50[:,3],bottom50[:,2],'*')
title("worst: corr = " + str(corr_coef(bottom50[:,3],bottom50[:,2])),fontsize=14)
xlabel("Turnover Rate")
ylabel("Free Throw Rate")

subplot(2,2,2)

plot(bottom50[:,4],bottom50[:,2],'*')
title("worst: corr = " + str(corr_coef(bottom50[:,4],bottom50[:,2])),fontsize=14)
xlabel("Offensive Rebound Rate")
ylabel("Free Throw Rate")

subplot(2,2,3)

plot(bottom50[:,4],bottom50[:,3],'*')
title("worst: corr = " + str(corr_coef(bottom50[:,4],bottom50[:,3])),fontsize=14)
xlabel("Offensive Rebound Rate")
ylabel("Turnover Rate")

       
show()






