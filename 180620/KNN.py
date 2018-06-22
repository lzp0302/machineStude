# -*- coding: UTF-8 -*- 
from numpy import *
import operator
if __name__ == '__main__':
	datingClassTest()
def main():
	print(11111)
def classify(intx,group,lables ,k):
	#group,lables=KNN.createDataSet()
	#groups2=array([[ 1.0 , 1.1 ] , [1.0,1.0], [0,0 ], [0,0.1]])
	dataSetSize=group.shape[0]
	#print(dataSetSize)
	diffmat=tile(intx,(dataSetSize,1))-group
	SqdiffMat=diffmat**2
	sqdistance=SqdiffMat.sum(axis=1)
	distance=sqdistance**0.5
	#print(distance)
	sortdistance=distance.argsort()
	classCount={}
	for i in range(k):
		lable=lables[sortdistance[i]]
		#print(lable)
		classCount[lable]=classCount.get(lable,0)+1
	#print(classCount)

	#print(classCount.iteritems())
	sortClassCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
	sortClassCount2=sorted(classCount.iteritems(),key=lambda class2:class2[1],reverse=True)
	#print(sortClassCount[0][0])
	#print(sortClassCount2[0][0])
	return sortClassCount
	
def createDataSet():
	groups=array([[ 1.0 , 1.1 ] , [1.0,1.0], [0,0 ], [0,0.1]])
	lables=[ ' b ' , 'b ' , ' a ' , 'a ']
	#lables=[1,1,2,2]
	return groups,lables

def file2matrix(filename):
	fr=open(filename)
	arrayOnlines=fr.readlines()
	numberoflines=len(arrayOnlines)
	returnMat=zeros((numberoflines,3))
	classVector=[]
	index=0
	for line in arrayOnlines:
		line=line.strip()
		listfromline=line.split("\t")
		returnMat[index,:]=listfromline[0:3]
		classVector.append(int(listfromline[-1]))
		index+=1
	return returnMat,classVector
#newValue ={ o l d V a l u e - m i n ) / (max-min)
def autoNorm(dataSet):
	minValues=dataSet.min(0)
	maxValues=dataSet.max(0)
	ranges=maxValues-minValues
	size=dataSet.shape[0]
	newDataSet=dataSet-tile(minValues,(size,1))
	newDataSet=newDataSet/(tile(ranges,(size,1)))
	return newDataSet,ranges,minValues

def datingClassTest():
	hoRatio=0.5
	datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')       #load data setfrom file
	normMat,ranges,minVals=autoNorm(datingDataMat)
	m=normMat.shape[0]
	numTestMat=int(hoRatio*m)
	erroCount=0
	for i in range(numTestMat):
		classResult=classify(normMat[i,:],normMat[numTestMat:m,:],datingLabels[numTestMat:m],3)
		print "the classifier came back with: %d, the real answer is: %d" % (classResult,datingLabels[i])
		#print("这个标本得到的类型为: %d实际类型为: %d" % (classResult,(datingLabels[i])))
		if(classResult !=datingLabels[i]):
			erroCount +=1.0
	
	print("这个算法的错误率为: %f"%(erroCount/(float)(numTestMat)))

