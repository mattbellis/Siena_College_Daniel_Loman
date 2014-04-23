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
eFGl=matrix([[0.0]*1]*210)
FTR1l=matrix([[0.0]*1]*210)
TORl=matrix([[0.0]*1]*210)
ORRl=matrix([[0.0]*1]*210)

startData=0
endData=210

index=0

N=len(lines)

for i in range(N):
    if((i >= startData) and (i < endData)):
        content=np.array(lines[i].split()).astype('float')
        OE[index,0]=content[0]
        eFGl[index,0]=content[1]/100
        FTR1l[index,0]=content[2]/10000
        TORl[index,0]=content[3]/100
        ORRl[index,0]=content[4]/100
        index=index+1

    

a=glob.glob('/Users/DanLo1108/Documents/AdvancedLab/Data Files/FTP.txt')
b=str(a[0])
infile=open(b,'r')
lines=infile.readlines()

FTPl=matrix([[0.0]*1]*210)

startData=0
endData=210

index=0

N=len(lines)

for i in range(N):
    if((i >= startData) and (i < endData)):
        content=np.array(lines[i].split()).astype('float')
        FTPl[index,0]=content[0]/100
        index=index+1

FTRl=matrix([[0.0]*1]*210)

for i in range(210):
    FTRl[i]=FTR1l[i]/FTPl[i]
    

################################################
###    FINDING STANDARD DEVIATION AND MEAN   ###
################################################

import StandardDeviation
from StandardDeviation import StandDev
from StandardDeviation import mean
from StandardDeviation import z_score

eFGsd=StandDev(eFGl)
FTRsd=StandDev(FTRl)
TORsd=StandDev(TORl)
ORRsd=StandDev(ORRl)
FTPsd=StandDev(FTPl)


eFGmean=mean(eFGl)
FTRmean=mean(FTRl)
TORmean=mean(TORl)
ORRmean=mean(ORRl)
FTPmean=mean(FTPl)

eFGz=matrix([[0.0]*1]*210)
FTRz=matrix([[0.0]*1]*210)
TORz=matrix([[0.0]*1]*210)
ORRz=matrix([[0.0]*1]*210)
FTPz=matrix([[0.0]*1]*210)

for i in range(len(eFGl)):
    eFGz[i]=z_score(eFGl[i],eFGmean,eFGsd)
    FTRz[i]=z_score(FTRl[i],FTRmean,FTRsd)
    TORz[i]=z_score(TORl[i],TORmean,TORsd)
    ORRz[i]=z_score(ORRl[i],ORRmean,ORRsd)
    FTPz[i]=z_score(FTPl[i],FTPmean,FTPsd)



### General Formula: FGA+.44*FTR+TOR=1.000

length=21

SD=np.array([0.0]*21)
ORarray=np.array([0.0]*length)

for i in range(len(SD)):
    SD[i]=.2*i-2

sims=1000    #Number of simulations run (100 poss = 1 simulation)

OffRatings=matrix([[0.0]*length]*sims)

for i in range(len(SD)):

    j=SD[i]
    

    ############################################################
    ###  Four Factors for an average NBA team in 2012-2013   ###
    ############################################################



    eFG=eFGmean+j*eFGsd     #Field goal percentage weighted for 3 point FGs
    FTR=FTRmean             #Free throw rate (FTA/FGA)
    TOR=TORmean             #Turnover rate (TO/poss)
    ORR=ORRmean            #Offensive rebound rate
    FTP=FTPmean             #League average FT%

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

    OR=OR+float(.3949*(eFGz[i]+1.78))
    OR=OR+float(.0812*(-1*TORz[i]+1.78))
    OR=OR+float(.2784*(FTRz[i]+1.78))
    OR=OR+float(.2454*(-1*ORRz[i]+1.78))

    ORarray[i]=OR

    print i
    #SD[i]=j
    


##error=np.array([0.0]*len(ORarray))
##
##for i in range(len(ORarray)):
##    error[i]=OE[i]-ORarray[i]
##
##
##import CorrelationCoefficient
##from CorrelationCoefficient import corr_coef
##
##
##eFGcorr=corr_coef(error,eFGz)
##FTRcorr=corr_coef(error,FTRz)
##TORcorr=corr_coef(error,TORz)
##ORRcorr=corr_coef(error,ORRz)
##
##import Bootstrap
##from Bootstrap import bootstrap
##
##eFGbs=bootstrap(error,eFGz)
##FTRbs=bootstrap(error,FTRz)
##TORbs=bootstrap(error,TORz)
##ORRbs=bootstrap(error,ORRz)
##
##
##total=eFGcorr+FTRcorr+fabs(TORcorr)+fabs(ORRcorr)
##
##eFGweight=eFGcorr/total
##FTRweight=FTRcorr/total
##TORweight=fabs(TORcorr)/total
##ORRweight=fabs(ORRcorr)/total





UC=np.array([0.0]*21)

for i in range(21):
    a=sorted(OffRatings[:,i])
    UC[i]=(a[(int(.84*len(OffRatings)))]-a[(int(.16*len(OffRatings)))])/2


slope,b=polyfit(SD,ORarray,1)
x=arange(-2,2.01,.2)
y=np.array([0.0]*21)

figure()
plot(SD,ORarray,'*')
#errorbar(SD,array(ORarray), yerr=array(UC), fmt='ro',label='68% confidence')
#legend(bbox_to_anchor=(0.50,.95),loc=6,borderaxespad=0,fontsize=16)
ylim(95,115)
xlabel('z score',fontsize=24)
ylabel('Offensive Efficiency (Pts/100 poss)',fontsize=24)
title('Effect of changing eFG% on OE',fontsize=30)
tickparams=tick_params(axis='both', length=5, labelsize=18)

for i in range(len(x)):
    y[i]=slope*x[i]+b

plot(x,y)

show()

print slope

