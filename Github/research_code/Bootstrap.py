import numpy as np
from numpy import linalg, matrix, array

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


