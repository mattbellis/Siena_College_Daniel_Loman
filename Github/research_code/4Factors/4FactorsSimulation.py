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

OE=matrix([[0.0]*1]*30)
eFGl=matrix([[0.0]*1]*30)
FTRl=matrix([[0.0]*1]*30)
TORl=matrix([[0.0]*1]*30)
ORRl=matrix([[0.0]*1]*30)

startData=0
endData=30

index=0

N=len(lines)

for i in range(N):
    if((i >= startData) and (i < endData)):
        content=np.array(lines[i].split()).astype('float')
        OE[index,0]=content[0]
        eFGl[index,0]=content[1]/100
        FTRl[index,0]=content[2]/100
        TORl[index,0]=content[3]/100
        ORRl[index,0]=content[4]/100
        index=index+1


a=glob.glob('/Users/DanLo1108/Documents/AdvancedLab/Data Files/FTP.txt')
b=str(a[0])
infile=open(b,'r')
lines=infile.readlines()

FTPl=matrix([[0.0]*1]*30)

startData=0
endData=30

index=0

N=len(lines)

for i in range(N):
    if((i >= startData) and (i < endData)):
        content=np.array(lines[i].split()).astype('float')
        FTPl[index,0]=content[0]/100
        index=index+1

FTpFGAl=matrix([[0.0]*1]*30)

for i in range(30):
    FTpFGAl[i]=FTRl[i]*FTPl[i]
    

################################################
###    FINDING STANDARD DEVIATION AND MEAN   ###
################################################

import StandardDeviation
from StandardDeviation import StandDev
from StandardDeviation import mean

eFGsd=StandDev(eFGl)
FTRsd=StandDev(FTRl)
TORsd=StandDev(TORl)
ORRsd=StandDev(ORRl)
FTPsd=StandDev(FTPl)
FTpFGAsd=StandDev(FTpFGAl)

eFGmean=mean(eFGl)
FTRmean=mean(FTRl)
TORmean=mean(TORl)
ORRmean=mean(ORRl)
FTPmean=mean(FTPl)
FTpFGAmean=mean(FTpFGAl)


### General Formula: FGA+.44*FTR+TOR=1.000

SD=np.array([0.0]*21)
ORarray=np.array([0.0]*21)

sims=10    #Number of simulations run (100 poss = 1 simulation)

OffRatings=matrix([[0.0]*21]*sims)

for i in range(21):

    j=.2*i-2

    ############################################################
    ###  Four Factors for an average NBA team in 2012-2013   ###
    ############################################################



    eFG=eFGmean+j*eFGsd       #Field goal percentage weighted for 3 point FGs
    FTR=FTRmean        #Free throw rate (FTA/FGA)
    TOR=TORmean        #Turnover rate (TO/poss)
    ORR=ORRmean        #Offensive rebound rate
    FTP=FTPmean        #League average FT%

    FGA=(1-TOR)/(1+.44*FTR)  # % of possessions that result in a field goal possession
    FTA=1-FGA-TOR            # % of possessions that result in free throws

    #############################
    ### POSSESSION SIMULATOR  ###
    #############################


    points=0 #total points scored
    points1=0
    poss=0   #total possessions
    FGM=0    #Field goals made
    FGAtt=0  #Field goals attempted



    count=0
    n=0
    while(poss<(100*sims)):
        import random
        a=random.random()
        if(a<FGA):
            b=random.random()
            if(b<eFG):
                points=points+2
                points1=points1+2
                poss=poss+1
    #            print 'Made shot!'
    #            print 'points: ' + str(points)
    #            print ' '
                FGM=FGM+1
                FGAtt=FGAtt+1
            else:
                c=random.random()
                if(c<ORR):
    #                print 'Missed shot'
    #                print 'Offensive Rebound!'
                    FGAtt=FGAtt+1
                else:
                    poss=poss+1
    #                print 'Missed shot'
    #                print 'points: ' + str(points)
    #                print ' '
                    FGAtt=FGAtt+1
        if(a>FGA and a<(FGA+FTA)):
            d=random.random()
            if(d<FTP):
                points=points+2
                points1=points1+2
                poss=poss+1
    #            print 'Made free throws!'
    #            print 'points: ' + str(points)
    #            print ' '
            else:
                e=random.random()
                if(e<ORR):
                    poss=poss
    #                print 'Missed free throw'
    #                print 'Offensive Rebound'
                else:
                    poss=poss+1
    #                print 'Missed free throw'
    #                print 'points: ' + str(points)
    #                print ' '
                    
        if(a>(FGA+FTA)):
            poss=poss+1
    #        print 'Turnover'
    #        print 'points: ' + str(points)
    #        print ' '


        if(count==99):
            OffRatings[poss/100,i]=points1
            points1=0
            count=0
        if(count<99):
            count=count+1
        

            

        
    FGP=float(FGM)/FGAtt #Field goal percentage

    OR=float(points)/sims   #Offensive Efficiency
    

    ORarray[i]=OR
    SD[i]=j


UC=np.array([0.0]*21)

for i in range(21):
    a=sorted(OffRatings[:,i])
    UC[i]=(a[(int(.95*len(OffRatings)))]-a[(int(.05*len(OffRatings)))])/2


slope,b=polyfit(SD,ORarray,1)

figure()
errorbar(SD,array(ORarray), yerr=array(UC), fmt='ro',label='95% confidence')
legend(bbox_to_anchor=(0.50,.95),loc=6,borderaxespad=0,fontsize=16)
xlabel=('z score')
ylabel=('Offensive Efficiency (Pts/100 poss)')
title=('Effect of changing eFG% on OE')
ylim(70,130)


show()

print slope
