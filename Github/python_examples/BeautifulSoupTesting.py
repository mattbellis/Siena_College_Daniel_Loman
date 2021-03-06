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


start=3

var0='TEAM'
passvar='RATE'      #COMP, PCT, YDS, YDS/A, LONG, TD, INT, SACK, YDSL, RATE, YDS/G
rushvar='YDS'      #ATT, YDS, YDS/A, LONG, TD, YDS/G, FUM, FUML
defpassvar='YDS/A'   #COMP, PCT, YDS, YDS/A, LONG, TD, INT, SACK, YDSL, RATE, YDS/G
defrushvar='TD'   #ATT, YDS, YDS/A, LONG, TD, YDS/G, FUM, FUML

years=['2012','2011','2010','2009','2008','2007','2006','2005','2004','2003','2002']      #2002-2012

passingstat=matrix([[0.0]*len(years)]*32)
rushingstat=matrix([[0.0]*len(years)]*32)
defpassingstat=matrix([[0.0]*len(years)]*32)
defrushingstat=matrix([[0.0]*len(years)]*32)
winpercent=matrix([[0.0]*len(years)]*32)

N=1000

CorrCoef=matrix([[0.0]*4]*len(years))
global CorrCoef1


################################################################################
# Correlation Coefficient function
################################################################################

def corr_coef(data1,data2):
       
    CorrCoef1=matrix([[0.0]*1]*N)
  
    normal=matrix([[0.0]*2]*len(data1))       #normalized pass/win pct data

    ave=matrix([[0.0]*2]*1)             #finding the mean of each dataset

    for i in range(len(normal)):
        ave[0,0]=ave[0,0]+data1[i]
        ave[0,1]=ave[0,1]+data2[i]

    ave=ave/32
    for i in range(32):
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

ranges=matrix([[0.0]*4]*len(years))
ranges1=matrix([[0.0]*1]*len(years))
zeroes=np.zeros(N)
CorrCoefarray=array([zeroes]*len(years))

def bootstrap(data1,data2):

    data=matrix([[0.0]*2]*32)
    data[:,0]=data1
    data[:,1]=data2

    ############################################################################
    # Create N1 fake data samples for the bootstrapping.
    ############################################################################
    zeroes=matrix([[0.0]*2]*32)
    newmatrix=matrix([[0.0]*2]*32)
    CorrCoefmatrix=matrix([[0.0]*1]*N)
    CorrCoefsorted=matrix([[0.0]*1]*int((N*.68)))
    matrixarray=array([zeroes]*N)
    for i in range(N):
        for j in range(32):
            a=random.randrange(0,32)
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
    
    for i in range(len(CorrCoefsorted)):
        CorrCoefsorted[i]=CorrCoefmatrix[i+(int(N*.16))]
    
    ranges1[year,0]=(CorrCoefsorted[len(CorrCoefsorted)-1]-CorrCoefsorted[0])/2


################################################################################

# Use this for the scatter plots.
fig_passscatter = figure(figsize=(8,8))

for year in range(len(years)):

    #####################################################
    #            ####PASSING STATISTICS####             #
    #####################################################
    
    r=requests.get('http://espn.go.com/nfl/statistics/team/_/stat/passing/year/'+years[year])

    data=r.content

    soup=BeautifulSoup(data)

    tables=soup.find_all('table')

    a = ["" for x in range(6000)]

    global count
    count=0

    class MyHTMLParser(HTMLParser):

        def handle_data(self,data):
            global count
            #print data
            a[count]=data
            count = count + 1
       
        
    parser=MyHTMLParser()
    parser.feed(str(tables))
    b=parser.handle_data(str(tables))


    dataarray=["" for x in range(start,count-1)]
    for i in range(count-start-1):
        dataarray[i]=a[i+start]

    dataarray=array(dataarray)


    ncols=14
    nrows=32

    nvalues=len(dataarray)-ncols
    for i in range(ncols):
        if(dataarray[i]=='TEAM'):
            index0=i
        if(dataarray[i]==passvar):
            index1=i

    indexes=np.arange(0,nvalues,ncols)
    datamatrix=matrix([["      "]*2]*(nrows))
    datamatrix1=matrix([["      "]*2]*(nrows))

    c=np.delete(dataarray[indexes+index0],0,None)
    d=np.delete(dataarray[indexes+index1],0,None)

    for i in range(len(c)):
        datamatrix[i,0]=c[i]
        datamatrix[i,1]=d[i]

    count1=0
    for a in sorted(datamatrix[:,0]):
        for i in range(32):
            if(a==datamatrix[i,0]):
                datamatrix1[count1,:]=datamatrix[i,:]
                count1=count1+1
            

    passingstat[:,year]=datamatrix1[:,1]




    #####################################################   
    #            ####RUSHING STATISTICS####             #
    #####################################################


    r=requests.get('http://espn.go.com/nfl/statistics/team/_/stat/rushing/year/'+years[year])

    data=r.content

    soup=BeautifulSoup(data)

    tables=soup.find_all('table')

    a = ["" for x in range(6000)]

    count=0

    class MyHTMLParser(HTMLParser):

        def handle_data(self,data):
            global count
            #print data
            a[count]=data
            count = count + 1
       
        
    parser=MyHTMLParser()
    parser.feed(str(tables))
    b=parser.handle_data(str(tables))


    dataarray=["" for x in range(start,count-1)]
    for i in range(count-start-1):
        dataarray[i]=a[i+start]

    dataarray=array(dataarray)


    ncols=10
    nrows=32

    nvalues=len(dataarray)-ncols
    for i in range(ncols):
        if(dataarray[i]=='TEAM'):
            index0=i
        if(dataarray[i]==rushvar):
            index1=i

    indexes=np.arange(0,nvalues,ncols)
    datamatrix=matrix([["      "]*2]*(nrows))
    datamatrix1=matrix([["      "]*2]*(nrows))

    c=np.delete(dataarray[indexes+index0],0,None)
    d=np.delete(dataarray[indexes+index1],0,None)

    for i in range(len(c)):
        datamatrix[i,0]=c[i]
        datamatrix[i,1]=d[i]

    count1=0
    for a in sorted(datamatrix[:,0]):
        for i in range(32):
            if(a==datamatrix[i,0]):
                datamatrix1[count1,:]=datamatrix[i,:]
                count1=count1+1
            

    rushingstat[:,year]=datamatrix1[:,1]


    #####################################################   
    #        ####DEF PASSING STATISTICS####             #
    #####################################################


    r=requests.get('http://espn.go.com/nfl/statistics/team/_/stat/passing/position/defense/year/'+years[year])

    data=r.content

    soup=BeautifulSoup(data)

    tables=soup.find_all('table')

    a = ["" for x in range(6000)]

    global count
    count=0

    class MyHTMLParser(HTMLParser):

        def handle_data(self,data):
            global count
            #print data
            a[count]=data
            count = count + 1
       
        
    parser=MyHTMLParser()
    parser.feed(str(tables))
    b=parser.handle_data(str(tables))


    dataarray=["" for x in range(start,count-1)]
    for i in range(count-start-1):
        dataarray[i]=a[i+start]

    dataarray=array(dataarray)


    ncols=14
    nrows=32

    nvalues=len(dataarray)-ncols
    for i in range(ncols):
        if(dataarray[i]=='TEAM'):
            index0=i
        if(dataarray[i]==defpassvar):
            index1=i

    indexes=np.arange(0,nvalues,ncols)
    datamatrix=matrix([["      "]*2]*(nrows))
    datamatrix1=matrix([["      "]*2]*(nrows))

    c=np.delete(dataarray[indexes+index0],0,None)
    d=np.delete(dataarray[indexes+index1],0,None)

    for i in range(len(c)):
        datamatrix[i,0]=c[i]
        datamatrix[i,1]=d[i]

    count1=0
    for a in sorted(datamatrix[:,0]):
        for i in range(32):
            if(a==datamatrix[i,0]):
                datamatrix1[count1,:]=datamatrix[i,:]
                count1=count1+1
            

    defpassingstat[:,year]=datamatrix1[:,1]
    

    
    #####################################################   
    #        ####DEF RUSHING STATISTICS####             #
    #####################################################


    r=requests.get('http://espn.go.com/nfl/statistics/team/_/stat/rushing/position/defense/year/'+years[year])

    data=r.content

    soup=BeautifulSoup(data)

    tables=soup.find_all('table')

    a = ["" for x in range(6000)]

    count=0

    class MyHTMLParser(HTMLParser):

        def handle_data(self,data):
            global count
            #print data
            a[count]=data
            count = count + 1
       
        
    parser=MyHTMLParser()
    parser.feed(str(tables))
    b=parser.handle_data(str(tables))


    dataarray=["" for x in range(start,count-1)]
    for i in range(count-start-1):
        dataarray[i]=a[i+start]

    dataarray=array(dataarray)


    ncols=10
    nrows=32

    nvalues=len(dataarray)-ncols
    for i in range(ncols):
        if(dataarray[i]=='TEAM'):
            index0=i
        if(dataarray[i]==defrushvar):
            index1=i

    indexes=np.arange(0,nvalues,ncols)
    datamatrix=matrix([["      "]*2]*(nrows))
    datamatrix1=matrix([["      "]*2]*(nrows))

    c=np.delete(dataarray[indexes+index0],0,None)
    d=np.delete(dataarray[indexes+index1],0,None)

    for i in range(len(c)):
        datamatrix[i,0]=c[i]
        datamatrix[i,1]=d[i]

    count1=0
    for a in sorted(datamatrix[:,0]):
        for i in range(32):
            if(a==datamatrix[i,0]):
                datamatrix1[count1,:]=datamatrix[i,:]
                count1=count1+1
            

    defrushingstat[:,year]=datamatrix1[:,1]




    #####################################################   
    #               ####WIN PERCENTAGE####              #
    #####################################################



    r=requests.get('http://espn.go.com/nfl/standings/_/year/'+years[year])

    data=r.content

    soup=BeautifulSoup(data)

    tables=soup.find_all('table')

    a = ["" for x in range(6000)]

    count=0

    class MyHTMLParser(HTMLParser):

        def handle_data(self,data):
            global count
            #print data
            a[count]=data
            count = count + 1
       
        
    parser=MyHTMLParser()
    parser.feed(str(tables))
    b=parser.handle_data(str(tables))


    dataarray=["" for x in range(start,count-1)]
    for i in range(count-start-1):
        dataarray[i]=a[i+start]

    dataarray=array(dataarray)

    dataarray = dataarray[dataarray!='\n']
    dataarray = dataarray[dataarray!='American Football Conference']
    dataarray = dataarray[dataarray!='x - ']
    dataarray = dataarray[dataarray!='y - ']
    dataarray = dataarray[dataarray!='z - ']
    dataarray = dataarray[dataarray!='* - ']


    ncols=13
    nrows=32

    nvalues=len(dataarray)-ncols
    for i in range(ncols):
        if(dataarray[i]=='NFC EAST'):
            index0=i
        if(dataarray[i]=='PCT'):
            index1=i

    indexes=np.arange(0,nvalues,ncols)
    indexes1=np.arange(0,40,5)

    datamatrix=matrix([["      "]*2]*(nrows))
    datamatrix1=matrix([["      "]*2]*(nrows))

    c=dataarray[indexes+index0]
    c=np.delete(c,indexes1,None)

    d=dataarray[indexes+index1]
    d=np.delete(d,indexes1,None)


    for i in range(len(c)):
        datamatrix[i,0]=c[i]
        datamatrix[i,1]=d[i]

    count1=0
    for a in sorted(datamatrix[:,0]):
        for i in range(32):
            if(a==datamatrix[i,0]):
                datamatrix1[count1,:]=datamatrix[i,:]
                count1=count1+1


    winpercent[:,year]=datamatrix1[:,1]

    # Plot the individual years for passing
    fig_passscatter.add_subplot(4,4,year+1)
    #print winpercent
    plot(winpercent[:,year],passingstat[:,year],'ko',markersize=5)
    title(years[year])
    xlabel('win PCT')
    ylabel(passvar)



for year in range(len(years)):
    bootstrap(passingstat[:,year],winpercent[:,year])
    corr_coef(passingstat[:,year],winpercent[:,year])
    CorrCoef[year,0]=CorrCoef1[0]
    ranges[year,0]=ranges1[year]


for year in range(len(years)):
    bootstrap(rushingstat[:,year],winpercent[:,year])
    corr_coef(rushingstat[:,year],winpercent[:,year])
    CorrCoef[year,1]=CorrCoef1[0]
    ranges[year,1]=ranges1[year]

for year in range(len(years)):
    bootstrap(defpassingstat[:,year],winpercent[:,year])
    corr_coef(defpassingstat[:,year],winpercent[:,year])
    CorrCoef[year,2]=CorrCoef1[0]
    ranges[year,2]=ranges1[year]


for year in range(len(years)):
    bootstrap(defrushingstat[:,year],winpercent[:,year])
    corr_coef(defrushingstat[:,year],winpercent[:,year])
    CorrCoef[year,3]=CorrCoef1[0]
    ranges[year,3]=ranges1[year]    


years2=array([0.0]*len(years)).astype('int')
for i in range(len(years)):
    years2[i]=float(years[i])



fig = figure()
plt.errorbar(years2, array(CorrCoef[:,0])[:,0], yerr=array(ranges[:,0])[:,0],fmt='ko')
xlabel('year')
ylabel('Correlation Coefficient')
title('Correlation between pass '+ passvar +' and win percent')
fmt_xdata = mdates.DateFormatter('%Y')
fig.autofmt_xdate()
ylim(-1.0,1.0)
xlim(min(years2)-1,max(years2)+1)
xrange(years2[0]-1, years2[len(years2)-1]+1)

figure()

plt.errorbar(years2, array(CorrCoef[:,1])[:,0], yerr=array(ranges[:,1])[:,0],fmt='ko')
xlabel('year')
ylabel('Correlation Coefficient')
title('Correlation between rush '+ rushvar + ' and win percent')
ylim(-1.0,1.0)
xlim(min(years2)-1,max(years2)+1)
xrange(years2[0]-1, years2[len(years2)-1]+1)

figure()

plt.errorbar(years2, array(CorrCoef[:,2])[:,0], yerr=array(ranges[:,2])[:,0],fmt='ko')
xlabel('year')
ylabel('Correlation Coefficient')
title('Correlation between def pass '+ defpassvar + ' and win percent')
ylim(-1.0,1.0)
xlim(min(years2)-1,max(years2)+1)
xrange(years2[0]-1, years2[len(years2)-1]+1)

figure()

plt.errorbar(years2, array(CorrCoef[:,3])[:,0], yerr=array(ranges[:,3])[:,0],fmt='ko')
xlabel('year')
ylabel('Correlation Coefficient')
title('Correlation between def rush '+ defrushvar + ' and win percent')
ylim(-1.0,1.0)
xlim(min(years2)-1,max(years2)+1)
xrange(years2[0]-1, years2[len(years2)-1]+1)

show()


avePass=0
aveRush=0
avePassRange=0
aveRushRange=0

avedefPass=0
avedefRush=0
avedefPassRange=0
avedefRushRange=0

for i in range(len(years)):
    avePass=avePass+CorrCoef[i,0]
    aveRush=aveRush+CorrCoef[i,1]
    avePassRange=avePassRange+ranges[i,0]
    aveRushRange=aveRushRange+ranges[i,1]
    
    avedefPass=avedefPass+CorrCoef[i,2]
    avedefRush=avedefRush+CorrCoef[i,3]
    avedefPassRange=avedefPassRange+ranges[i,2]
    avedefRushRange=avedefRushRange+ranges[i,3]

    
avePass=avePass/len(years)
aveRush=aveRush/len(years)
avePassRange=avePassRange/len(years)
aveRushRange=aveRushRange/len(years)

avedefPass=avedefPass/len(years)
avedefRush=avedefRush/len(years)
avedefPassRange=avedefPassRange/len(years)
avedefRushRange=avedefRushRange/len(years)

print 'avePass: ' + str(avePass)
print 'aveRush: ' + str(aveRush)
print 'avePassRange: ' + str(avePassRange)
print 'aveRushRange: ' + str(aveRushRange)

print 'avedefPass: ' + str(avedefPass)
print 'avedefRush: ' + str(avedefRush)
print 'avedefPassRange: ' + str(avedefPassRange)
print 'avedefRushRange: ' + str(avedefRushRange)
