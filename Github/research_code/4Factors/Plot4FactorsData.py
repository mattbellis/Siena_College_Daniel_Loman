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
FTR=matrix([[0.0]*1]*210)
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
        FTR[index,0]=content[2]/10000
        TOR[index,0]=content[3]/100
        ORR[index,0]=content[4]/100
        index=index+1


a=glob.glob('/Users/DanLo1108/Documents/AdvancedLab/Data Files/FTP.txt')
b=str(a[0])
infile=open(b,'r')
lines=infile.readlines()



Y=matrix([[0.0]*5]*210)

for i in range(len(Y)):

    Y[i,0]=OE[i]
    Y[i,1]=eFG[i]
    Y[i,2]=FTR[i]
    Y[i,3]=TOR[i]
    Y[i,4]=ORR[i]

Y=array(Y)
Y1=sorted(Y, key=lambda Y_entry: Y_entry[0])

top25=matrix([[0.0]*5]*53)
bottom25=matrix([[0.0]*5]*53)
mid50=matrix([[0.0]*5]*104)

for i in range(len(top25)):

        top25[i,0]=Y1[209-i][0]
        top25[i,1]=Y1[209-i][1]
        top25[i,2]=Y1[209-i][2]
        top25[i,3]=Y1[209-i][3]
        top25[i,4]=Y1[209-i][4]

        bottom25[i,0]=Y1[i][0]
        bottom25[i,1]=Y1[i][1]
        bottom25[i,2]=Y1[i][2]
        bottom25[i,3]=Y1[i][3]
        bottom25[i,4]=Y1[i][4]
        

for i in range(len(mid50)):
    
        mid50[i,0]=Y1[i+53][0]
        mid50[i,1]=Y1[i+53][1]
        mid50[i,2]=Y1[i+53][2]
        mid50[i,3]=Y1[i+53][3]
        mid50[i,4]=Y1[i+53][4]


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
#subplot(2,2,1)


plot(eFG,OE,'*')
#title("all: correlation = " + str(eFG_OEcorr),fontsize=14)
xlabel("Effective Field Goal Percentage",fontsize=24)
ylabel("Offensive Efficiency",fontsize=24)
title("eFG% vs OE", fontsize=30)
tickparams=tick_params(axis='both', length=5, labelsize=18)

#subplot(2,2,2)
figure()

plot(FTR,OE,'*')
#title("all: correlation = " + str(FTR_OEcorr),fontsize=14)
xlabel("Free Throw Rate",fontsize=24)
ylabel("Offensive Efficiency",fontsize=24)
title("FTR vs OE",fontsize=30)
tickparams=tick_params(axis='both', length=5, labelsize=18)

#subplot(2,2,3)
figure()

plot(TOR,OE,'*')
#title("all: correlation = " + str(TOR_OEcorr),fontsize=14)
xlabel("Turnover Rate",fontsize=24)
ylabel("Offensive Efficiency",fontsize=24)
title("TOR vs OE", fontsize=30)
tickparams=tick_params(axis='both', length=5, labelsize=18)

#subplot(2,2,4)
figure()

plot(ORR,OE,'*')
#title("all: corr= " + str(ORR_OEcorr),fontsize=14)
xlabel("Offensive Rebound Rate",fontsize=24)
ylabel("Offensive Efficiency",fontsize=24)
title("ORR vs OE", fontsize=30)
tickparams=tick_params(axis='both', length=5, labelsize=18)

############################################################
##### eFG on Y axis

      
figure()


plot(top25[:,2],top25[:,1],'g*')
plot(bottom25[:,2],bottom25[:,1],'r*')
plot(mid50[:,2],mid50[:,1],'b*')
plot(.2528,.5211,'o',markerfacecolor='g',markeredgecolor='k',markersize=12)
plot(.2107,.4763,'o',markerfacecolor='r',markeredgecolor='k',markersize=12)
plot(.1473,.4763,'o',markerfacecolor='r',markeredgecolor='k',markersize=12)
title("FTR vs eFG%",fontsize=30)
xlabel("Free Throw Rate",fontsize=24)
ylabel("Effective Field Goal Percentage",fontsize=24)
tickparams=tick_params(axis='both', length=5, labelsize=18)

figure()

plot(top25[:,3],top25[:,1],'g*')
plot(bottom25[:,3],bottom25[:,1],'r*')
plot(mid50[:,3],mid50[:,1],'b*')
plot(.1350,.5211,'o',markerfacecolor='g',markeredgecolor='k',markersize=12)
plot(.1406,.4763,'o',markerfacecolor='r',markeredgecolor='k',markersize=12)
plot(.1310,.4763,'o',markerfacecolor='r',markeredgecolor='k',markersize=12)
title("TOR vs eFG%",fontsize=30)
xlabel("Turnover Rate",fontsize=24)
ylabel("Effective Field Goal Percentage",fontsize=24)
tickparams=tick_params(axis='both', length=5, labelsize=18)

figure()

plot(top25[:,4],top25[:,1],'g*')
plot(bottom25[:,4],bottom25[:,1],'r*')
plot(mid50[:,4],mid50[:,1],'b*')
plot(.2650,.5211,'o',markerfacecolor='g',markeredgecolor='k',markersize=12)
plot(.2774,.4763,'o',markerfacecolor='r',markeredgecolor='k',markersize=12)
plot(.2513,.4763,'o',markerfacecolor='r',markeredgecolor='k',markersize=12)
title("ORR vs eFG%",fontsize=30)
xlabel("Offensive Rebound Rate",fontsize=24)
ylabel("Effective Field Goal Percentage",fontsize=24)
tickparams=tick_params(axis='both', length=5, labelsize=18)

#########################################################
##### FTR and TOR on Y axis

figure()


plot(top25[:,3],top25[:,2],'g*')
plot(bottom25[:,3],bottom25[:,2],'r*')
plot(mid50[:,3],mid50[:,2],'b*')
plot(.1350,.2528,'o',markerfacecolor='g',markeredgecolor='k',markersize=12)
plot(.1406,.2107,'o',markerfacecolor='r',markeredgecolor='k',markersize=12)
plot(.1310,.1473,'o',markerfacecolor='r',markeredgecolor='k',markersize=12)
title("TOR vs FTR",fontsize=30)
xlabel("Turnover Rate",fontsize=24)
ylabel("Free Throw Rate",fontsize=24)
tickparams=tick_params(axis='both', length=5, labelsize=18)

figure()

plot(top25[:,4],top25[:,2],'g*')
plot(bottom25[:,4],bottom25[:,2],'r*')
plot(mid50[:,4],mid50[:,2],'b*')
plot(.2650,.2528,'o',markerfacecolor='g',markeredgecolor='k',markersize=14)
plot(.2774,.2107,'o',markerfacecolor='r',markeredgecolor='k',markersize=14)
plot(.2513,.1473,'o',markerfacecolor='r',markeredgecolor='k',markersize=14)
title("ORR vs FTR",fontsize=30)
xlabel("Offensive Rebound Rate",fontsize=24)
ylabel("Free Throw Rate",fontsize=24)
tickparams=tick_params(axis='both', length=5, labelsize=18)

figure()

plot(top25[:,4],top25[:,3],'g*')
plot(bottom25[:,4],bottom25[:,3],'r*')
plot(mid50[:,4],mid50[:,3],'b*')
plot(.2650,.1350,'o',markerfacecolor='g',markeredgecolor='k',markersize=14)
plot(.2774,.1406,'o',markerfacecolor='r',markeredgecolor='k',markersize=14)
plot(.2513,.1310,'o',markerfacecolor='r',markeredgecolor='k',markersize=14)
title("ORR vs TOR",fontsize=30)
xlabel("Offensive Rebound Rate",fontsize=24)
ylabel("Turnover Rate",fontsize=24)
tickparams=tick_params(axis='both', length=5, labelsize=18)

show()






