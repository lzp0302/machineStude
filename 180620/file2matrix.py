from numpy  import *
def file2matix2(filename):
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
