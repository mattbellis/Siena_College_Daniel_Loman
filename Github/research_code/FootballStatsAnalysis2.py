import requests
from bs4 import BeautifulSoup
import re
import numpy as np
from numpy import linalg, matrix, array
import HTMLParser
from HTMLParser import HTMLParser
import math
import pylab
from pylab import *
import random

import matplotlib.dates as mdates



var0='TEAM'
passvar='Yds'      #Cmp, Att, Yds, TD, Int, NY/A, 1stD
rushvar='Yds'      #Att, Yds, TD, Y/A, 1stD
defpassvar='Yds'   #Cmp, Att, Yds, TD, Int, NY/A, 1stD
defrushvar='Yds'   #Att, Yds, TD, Y/A, 1stD


years=[0.0]*43  #enters desired number of years to analyze
j=0
for i in range(1970,2013):
    years[j]=str(i)
    j=j+1



datamatrix=matrix([['                       ']*2]*32)

CorrCoef=matrix([[0.0]*4]*len(years))
global CorrCoef1

avepassyards=matrix([[0.0]*1]*len(years))
averushyards=matrix([[0.0]*1]*len(years))
avedefpassyards=matrix([[0.0]*1]*len(years))
avedefrushyards=matrix([[0.0]*1]*len(years))

#####################################################
#     ####Defining Correlation Coefficient####      #
#####################################################

def corr_coef(data1,data2):

    M=len(data1)
       
    CorrCoef1=matrix([[0.0]*1]*N)
  
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

    global CorrCoef1
    CorrCoef1[0]=Corr[0,1]



################################################################################
# Bootstrap method function
################################################################################

N=1000 #Number of iterations for bootstrap method

ranges69=matrix([[0.0]*4]*len(years))
ranges95=matrix([[0.0]*4]*len(years))
ranges1=matrix([[0.0]*1]*len(years))
ranges2=matrix([[0.0]*1]*len(years))
zeroes=np.zeros(N)
CorrCoefarray=array([zeroes]*len(years))

def bootstrap(data1,data2):

    M=len(data1)
    data=matrix([[0.0]*2]*M)
    data[:,0]=data1
    data[:,1]=data2

    ############################################################################
    # Create N1 fake data samples for the bootstrapping.
    ############################################################################
    zeroes=matrix([[0.0]*2]*M)
    newmatrix=matrix([[0.0]*2]*M)
    CorrCoefmatrix=matrix([[0.0]*1]*N)
    CorrCoefsorted1=matrix([[0.0]*1]*int((N*.68)))
    CorrCoefsorted2=matrix([[0.0]*1]*int((N*.95)))
    matrixarray=array([zeroes]*N)
    for i in range(N):
        for j in range(M):
            a=random.randrange(0,M)
            newmatrix[j,0]=data[a,0]
            newmatrix[j,1]=data[a,1]

        matrixarray[i]=newmatrix
        
    global CorrCoef1

    ############################################################################
    # Calculate the corr coeff for *each* boostrap sample.
    ############################################################################
    for i in range(N):

        corr_coef(matrixarray[i,:,0].T,matrixarray[i,:,1].T)
        CorrCoefmatrix[i]=CorrCoef1[0]

    
    CorrCoefmatrix=sorted(CorrCoefmatrix)
    
    for i in range(len(CorrCoefsorted1)):
        CorrCoefsorted1[i]=CorrCoefmatrix[i+(int(N*.16))]

    for i in range(len(CorrCoefsorted2)):
        CorrCoefsorted2[i]=CorrCoefmatrix[i+(int(N*.025))]
    
    ranges1[year,0]=(CorrCoefsorted1[len(CorrCoefsorted1)-1]-CorrCoefsorted1[0])/2
    ranges2[year,0]=(CorrCoefsorted2[len(CorrCoefsorted2)-1]-CorrCoefsorted2[0])/2



################################################################################

# Use this for the scatter plots.
fig_passscatter = figure(figsize=(8,8))

for year in range(len(years)):

    r1=requests.get('http://www.pro-football-reference.com/years/'+years[year])
    r2=requests.get('http://www.pro-football-reference.com/years/'+years[year]+'/opp.htm')

    data1=r1.content
    soup1=BeautifulSoup(data1)
    table1=soup1.find_all('table')

    data2=r2.content
    soup2=BeautifulSoup(data2)
    table2=soup2.find_all('table')

    if(float(years[year])<=2002):
        tab=5
    if(float(years[year])==2011):
        tab=6
    if(float(years[year])>2002 and float(years[year])<=2010 and float(years[year])!=2006):
        tab=8
    if(float(years[year])==2006 or float(years[year])==2012):
        tab=9

    wintable=table1[0]
    offtable=table1[tab]
    deftable=table2[0]


    winrows=wintable.findAll('tr')
    offrows=offtable.findAll('tr')
    defrows=deftable.findAll('tr')

    #####################################################
    #               ####WIN PERCENTAGE####              #
    #####################################################
    

    values=['Tm', 'W', 'L', 'T','W-L%', 'Pts', 'PtsO','PtDef','MoV','SoS','SRS','OSRS','DSRS']

    val1='Tm'
    val2='W-L%'

    val_index1=values.index(val1)
    val_index2=values.index(val2)

    count=0

    for row in winrows:
        columns=row.findAll('td')
        for i, column1 in enumerate(columns):
            for j, column2 in enumerate(columns):
                if i==val_index1 and j== val_index2 and column1.text != val1 and column2.text != val2:
                    if(column1.text != '' and column2.text != ''):
                         datamatrix[count,0] = column1.text
                         datamatrix[count,1] = column2.text
                         count=count+1
                         
    datamatrix1=matrix([["                     "]*2]*count)

    count1=0
    for a in sorted(datamatrix[:,0]):
        for i in range(len(datamatrix1)):
            if(a==datamatrix[i,0]):
                datamatrix1[count1,:]=datamatrix[i,:]
                count1=count1+1

    winpercent=matrix([[0.0]*len(years)]*len(datamatrix1))

    for i in range(len(datamatrix1)):
        winpercent[i,year]=float(datamatrix1[i,1])


    #####################################################
    #         ####PASSING/RUSHING YARDS####             #
    #####################################################

    values1=['Rk','Tm','G','Pts','Yds','Ply','Y/P','TO','FL','1stPy','1stD','Cmp','Att','Yds','TD','Int','NY/A','1stD','Att','Yds','TD','Y/A','1stD','Sc%','TO%','EXP']
    values2=['Rk','Tm','G','Pts','Yds','Ply','Y/P','1stD','Cmp','Att','Yds','TD','Int','NY/A','1stD','Att','Yds','TD','Y/A','1stD','Sc%','TO%','EXP']

    b=float(years[year])
    
    if(b>2000):
        values=values1
    if(b<=2000.0):
        values=values2


    val1='Tm'
    val2=passvar
    val3=rushvar

    val_index1=values.index(val1)
    val_index2=0
    val_index3=0

    for i in range(5,len(values)):
        if(val_index2==0):
            if(values[i]==val2):
                val_index2=i
        if(values[i]==val2 and val_index2 != i):
            val_index3=i

    count=0

    for row in offrows:
        columns=row.findAll('td')
        for i, column1 in enumerate(columns):
            for j, column2 in enumerate(columns):
                if i==val_index1 and j== val_index2 and column1.text != val1 and column2.text != val2:
                    if(column1.text != '' and column2.text != '' and column1.text != 'Avg Team' and column1.text != 'League Total' and column1.text != 'Avg Tm/G'):
                         datamatrix[count,0] = column1.text
                         datamatrix[count,1] = column2.text
                         count=count+1

                         
    datamatrix1=matrix([["                    "]*2]*count)

    count1=0
    for a in sorted(datamatrix[:,0]):
        for i in range(len(datamatrix1)):
            if(a==datamatrix[i,0]):
                datamatrix1[count1,:]=datamatrix[i,:]
                count1=count1+1

    passingstat=matrix([[0.0]*1]*len(datamatrix1))

    for i in range(len(datamatrix1)):
        passingstat[i]=float(datamatrix1[i,1])

    count=0
    datamatrix=matrix([['                  ']*2]*32)
    
    for row in offrows:
        columns=row.findAll('td')
        for i, column1 in enumerate(columns):
            for j, column2 in enumerate(columns):
                if i==val_index1 and j== val_index3 and column1.text != val1 and column2.text != val3:
                    if(column1.text != '' and column2.text != '' and column1.text != 'Avg Team' and column1.text != 'League Total' and column1.text != 'Avg Tm/G'):
                         datamatrix[count,0] = column1.text
                         datamatrix[count,1] = column2.text
                         count=count+1
                         


    datamatrix1=matrix([["                  "]*2]*count)

    count1=0
    for a in sorted(datamatrix[:,0]):
        for i in range(len(datamatrix1)):
            if(a==datamatrix[i,0]):
                datamatrix1[count1,:]=datamatrix[i,:]
                count1=count1+1

    rushingstat=matrix([[0.0]*1]*len(datamatrix1))

    for i in range(len(datamatrix1)):
        rushingstat[i]=float(datamatrix1[i,1])


    #####################################################
    #                  ####DEFENSE####                  #
    #####################################################

     
    val1='Tm'
    val2=defpassvar
    val3=defrushvar

    val_index1=values.index(val1)
    val_index2=0
    val_index3=0

    for i in range(5,len(values)):
        if(val_index2==0):
            if(values[i]==val2):
                val_index2=i
        if(values[i]==val2 and val_index2 != i):
            val_index3=i

    count=0

    for row in defrows:
        columns=row.findAll('td')
        for i, column1 in enumerate(columns):
            for j, column2 in enumerate(columns):
                if i==val_index1 and j== val_index2 and column1.text != val1 and column2.text != val2:
                    if(column1.text != '' and column2.text != '' and column1.text != 'Avg Team' and column1.text != 'League Total' and column1.text != 'Avg Tm/G'):
                         datamatrix[count,0] = column1.text
                         datamatrix[count,1] = column2.text
                         count=count+1

                         
    datamatrix1=matrix([["                  "]*2]*count)

    count1=0
    for a in sorted(datamatrix[:,0]):
        for i in range(len(datamatrix1)):
            if(a==datamatrix[i,0]):
                datamatrix1[count1,:]=datamatrix[i,:]
                count1=count1+1

    defpassingstat=matrix([[0.0]*1]*len(datamatrix1))

    for i in range(len(datamatrix1)):
        defpassingstat[i]=float(datamatrix1[i,1])

    count=0
    datamatrix=matrix([['                  ']*2]*32)
    
    for row in defrows:
        columns=row.findAll('td')
        for i, column1 in enumerate(columns):
            for j, column2 in enumerate(columns):
                if i==val_index1 and j== val_index3 and column1.text != val1 and column2.text != val3:
                    if(column1.text != '' and column2.text != '' and column1.text != 'Avg Team' and column1.text != 'League Total' and column1.text != 'Avg Tm/G'):
                         datamatrix[count,0] = column1.text
                         datamatrix[count,1] = column2.text
                         count=count+1


    datamatrix1=matrix([["                  "]*2]*count)

    count1=0
    for a in sorted(datamatrix[:,0]):
        for i in range(len(datamatrix1)):
            if(a==datamatrix[i,0]):
                datamatrix1[count1,:]=datamatrix[i,:]
                count1=count1+1

    defrushingstat=matrix([[0.0]*1]*len(datamatrix1))

    for i in range(len(datamatrix1)):
        defrushingstat[i]=float(datamatrix1[i,1])


    ### FINDS CORRELATION AND UNCERTAINTIES FOR THE STATS ###

    print 'Extracting passing data for ' + years[year] + '...'
    bootstrap(passingstat[:],winpercent[:,year])
    corr_coef(passingstat[:],winpercent[:,year])
    CorrCoef[year,0]=CorrCoef1[0]
    ranges69[year,0]=ranges1[year]
    ranges95[year,0]=ranges2[year]
    

    print 'Extracting rushing data for ' + years[year] + '...'
    bootstrap(rushingstat[:],winpercent[:,year])
    corr_coef(rushingstat[:],winpercent[:,year])
    CorrCoef[year,1]=CorrCoef1[0]
    ranges69[year,1]=ranges1[year]
    ranges95[year,1]=ranges2[year]
    

    print 'Extracting defensive passing data for ' + years[year] + '...'
    bootstrap(defpassingstat[:],winpercent[:,year])
    corr_coef(defpassingstat[:],winpercent[:,year])
    CorrCoef[year,2]=CorrCoef1[0]
    ranges69[year,2]=ranges1[year]
    ranges95[year,2]=ranges2[year]


    print 'Extracting defensive rushing data for ' + years[year] + '...'
    bootstrap(defrushingstat[:],winpercent[:,year])
    corr_coef(defrushingstat[:],winpercent[:,year])
    CorrCoef[year,3]=CorrCoef1[0]
    ranges69[year,3]=ranges1[year]
    ranges95[year,3]=ranges2[year]


    ### FINDS AVERAGE VALUES FOR THE STATISTICS ###

    avepass=0
    averush=0

    for i in range(len(passingstat)):
        avepass=avepass+passingstat[i]
        averush=averush+rushingstat[i]


    avepassyards[year]=avepass/len(passingstat)
    averushyards[year]=averush/len(rushingstat)


    if(float(years[year])<1978):
        avepassyards[year]=avepassyards[year]/14
        averushyards[year]=averushyards[year]/14
    if(float(years[year])>=1978 and float(years[year])!= 1982 and float(years[year])!=1987):
        avepassyards[year]=avepassyards[year]/16
        averushyards[year]=averushyards[year]/16
    if(float(years[year])==1982):
        avepassyards[year]=avepassyards[year]/9
        averushyards[year]=averushyards[year]/9
    if(float(years[year])==1987):
        avepassyards[year]=avepassyards[year]/15
        averushyards[year]=averushyards[year]/15


    ### SAVES AVERAGE VALUES TO A TEXT FILE ###

    exportFolder='/Users/DanLo1108/Documents/Python programs/Exported Python Files/'
        
    np.savetxt(exportFolder+'PASSYDS.txt',avepassyards, delimiter="\t")
    np.savetxt(exportFolder+'RUSHYDS.txt',averushyards, delimiter="\t")

    

    ### PLOTS CORRELATION COEFFICIENTS AND THEIR UNCERTAINTIES ###

years2=array([0.0]*len(years)).astype('int')
for i in range(len(years)):
    years2[i]=float(years[i])

fig = figure()



plt.errorbar(years2, array(CorrCoef[:,0])[:,0], yerr=array(ranges95[:,0])[:,0],fmt='ro',label='95% confidence')
plt.errorbar(years2, array(CorrCoef[:,0])[:,0], yerr=array(ranges69[:,0])[:,0],fmt='ko',label='69% confidence')
legend(bbox_to_anchor=(0.50,.15),loc=6,borderaxespad=0,fontsize=16)
xlabel('year',fontsize=20)
ylabel('Correlation Coefficient',fontsize=20)
title('Correlation between pass '+ passvar +' and win percent',fontsize=20)
fmt_xdata = mdates.DateFormatter('%Y')
fig.autofmt_xdate()
ylim(-1.0,1.0)
xlim(min(years2)-1,max(years2)+1)
xrange(years2[0]-1, years2[len(years2)-1]+1)
fmt_xdata = mdates.DateFormatter('%Y')
fig.autofmt_xdate()

figure()

plt.errorbar(years2, array(CorrCoef[:,1])[:,0], yerr=array(ranges95[:,1])[:,0],fmt='ro',label='95% confidence')
plt.errorbar(years2, array(CorrCoef[:,1])[:,0], yerr=array(ranges69[:,1])[:,0],fmt='ko',label='69% confidence')
legend(bbox_to_anchor=(0.50,.15),loc=6,borderaxespad=0,fontsize=16)
xlabel('year',fontsize=20)
ylabel('Correlation Coefficient',fontsize=20)
title('Correlation between rush '+ rushvar + ' and win percent',fontsize=20)
ylim(-1.0,1.0)
xlim(min(years2)-1,max(years2)+1)
xrange(years2[0]-1, years2[len(years2)-1]+1)

figure()

plt.errorbar(years2, array(CorrCoef[:,2])[:,0], yerr=array(ranges95[:,2])[:,0],fmt='ro',label='95% confidence')
plt.errorbar(years2, array(CorrCoef[:,2])[:,0], yerr=array(ranges69[:,2])[:,0],fmt='ko',label='69% confidence')
legend(bbox_to_anchor=(0.50,.90),loc=6,borderaxespad=0,fontsize=16)
xlabel('year', fontsize=20)
ylabel('Correlation Coefficient',fontsize=20)
title('Correlation between def pass '+ defpassvar + ' and win percent', fontsize=20)
ylim(-1.0,1.0)
xlim(min(years2)-1,max(years2)+1)
xrange(years2[0]-1, years2[len(years2)-1]+1)

figure()

plt.errorbar(years2, array(CorrCoef[:,3])[:,0], yerr=array(ranges95[:,3])[:,0],fmt='ro',label='95% confidence')
plt.errorbar(years2, array(CorrCoef[:,3])[:,0], yerr=array(ranges69[:,3])[:,0],fmt='ko',label='69% confidence')
legend(bbox_to_anchor=(0.50,.85),loc=6,borderaxespad=0,fontsize=16)
xlabel('year',fontsize=20)
ylabel('Correlation Coefficient',fontsize=20)
title('Correlation between def rush '+ defrushvar + ' and win percent',fontsize=20)
ylim(-1.0,1.0)
xlim(min(years2)-1,max(years2)+1)
xrange(years2[0]-1, years2[len(years2)-1]+1)


show()
