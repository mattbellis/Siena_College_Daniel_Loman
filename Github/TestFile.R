library(boot)

mydata = scan("/Users/DanLo1108/Documents/AdvancedLab/Data Files/teamStats_1.csv") #scans csv or txt file, each value = 1 index (starts at 1)

numcols=5    # number of columns
numrows=210  #number of rows
len=length(mydata) #length of mydata

OE=rep(0,210) #array of 0's, length 210
eFG=rep(0,210)
FTR=rep(0,210)
TOR=rep(0,210)
ORR=rep(0,210)

count=1
for (i in 1:len){  #filling arrays
	if (i%%5==1){
		OE[count]=mydata[i]
	}
	if (i%%5==2){
		eFG[count]=mydata[i]/100
	}
	if (i%%5==3){
		FTR[count]=mydata[i]/10000
	}
	if (i%%5==4){
		TOR[count]=mydata[i]/100
	}
	if (i%%5==0){
		ORR[count]=mydata[i]/100
		count=count+1
	}
	
}
#print(cor(OE,eFG))
#print(cor(OE,FTR))
#print(cor(OE,TOR))
#print(cor(OE,ORR))

print("eFG% vs OE : ")
print(boot(c(eFG,OE),statistic=cor,R=1000)) #bootstrapping, shows correlation with error
print("FTR vs OE : ") #original = correlation, std error = bootstrap
print(boot(c(FTR,OE),statistic=cor,R=1000))
print("TOR vs OE : ")
print(boot(c(TOR,OE),statistic=cor,R=1000))
print("ORR vs OE : ")
print(boot(c(ORR,OE),statistic=cor,R=1000))


plot(eFG,OE)
#plot(eFG,FTR)
#plot(eFG,TOR)
#plot(eFG,ORR)

#can only plot once at a time
