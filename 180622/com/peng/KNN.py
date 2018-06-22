# -*- coding: UTF-8 -*-
import operator
from os import listdir
from numpy import *
#将图片转为矢量存储起来
def image2Matric(fileName):
    returnVector=zeros((1,1024))
    fr=open(fileName)
    for i in range(32):
        str=fr.readline()
        for j in range(32):
            returnVector[0,32*i+j]=str[j]
    return returnVector
#/home/peng/work/code/AI/machineStude/180622/com/peng/digits/trainingDigits/0_5.txt
#讲本地的标本解析成测试数据
def handWritingClassTest():
    fileList=listdir('digits/trainingDigits')
    lenNum=len(fileList)
    hdlables=[]
    dataMat=zeros((lenNum,1024))

    for i in range(lenNum):
        fileName=fileList[i]
        lable=fileName.split('_')[0]
        hdlables.append(lable)

        mat=image2Matric('digits/trainingDigits/%s'%fileName)
        dataMat[i,:]=mat

    fileListTest=listdir('digits/testDigits')
    lenNumTest=len(fileListTest)

    erroNumber=0
    for j in range(lenNumTest):
        fileNameTest=fileListTest[j]
        lable = (int)(fileNameTest.split('_')[0])

        mat = image2Matric('digits/testDigits/%s'%fileNameTest)
        classEcpect=(int)(classify(mat,dataMat,hdlables,5))
        print('lable ==%d class%d'%(lable,classEcpect))
        if(lable!=classEcpect):
            erroNumber+=1.0
    print("算法的错误率为: %d"%(erroNumber/lenNumTest))

def classify(intx,group,lables ,k):
    dataSetSize=group.shape[0]
    diffmat=tile(intx,(dataSetSize,1))-group
    SqdiffMat=diffmat**2
    sqdistance=SqdiffMat.sum(axis=1)
    distance=sqdistance**0.5
    sortdistance=distance.argsort()
    classCount={}
    for i in range(k):
        lable=lables[sortdistance[i]]
        classCount[lable]=classCount.get(lable,0)+1

    sortClassCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortClassCount[0][0]

if __name__ == '__main__':
    #mat=image2Matric('digits/trainingDigits/0_1.txt')
    handWritingClassTest()
