from numpy import *
import operator
def createDataSet():
	groups=array([[ 1.0 , 1.1 ] , [1.0,1.0], [0,0 ], [0,0.1]])
	lables=[ ' b ' , 'b ' , ' a ' , 'a ']
	#lables=[1,1,2,2]
	return groups,lables

