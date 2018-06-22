# -*- coding: UTF-8 -*- 
from numpy import *
import operator
# square  平方
# distance 距离
def classify(intx,group,lables ,k):
	dataSetSize=group.shape[0]
	diffmat=tile(intx,(dataSetSize,1))-group
	SqdiffMat=diffmat**2
	sqdistance=SqdiffMat.sum(axis=1)
	distance=sqdistance**0.5
	#print(distance)
	sortdistance=distance.argsort()
	classCount={}
	for i in range(k):
		lable=lables[sortdistance[i]]
		classCount[lable]=classCount.get(lable,0)+1
	sortClassCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
	sortClassCount2=sorted(classCount.iteritems(),key=lambda class2:class2[1],reverse=True)
	return sortClassCount[0][0]

