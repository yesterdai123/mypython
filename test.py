from numpy import *

#目标函数系数列向量
c = [1,-3,-1,0,0,0]

#约束条件系数矩阵
A = array([[3,-1,2,1,0,0],
           [-2,4,0,0,1,0],
           [-4,3,8,0,0,1]])
#约束右端项
b = [7,12,10]
#判别数向量
j = [-1,3,1,-1,-1,-1]

#行列数
cols = 6
rows = 3

#当前各个基变量、非基变量在A中的位置
dispositionB = [0,0,0,1,2,3,]

#基变量个数
numB = 3
#非基变量个数
numFB = 3
#最优基本可行解
ans = [0,0,0]

#打印信息
def printMessage():
    for i in range(numB+numFB):
        print(dispositionB[i],end=' ')
    print()

#更新约束条件系数矩阵
def updateA(colIndex,rowIndex):
    factor = array([0.0,0.0,0.0])
    ind = 0
    for n in range(rows):
        if(n == rowIndex):
            continue
        else:
            print("caculate factor")
            print(A[n][colIndex],end=' ')
            print(A[rowIndex][colIndex])
            factor[ind] = float(A[n][colIndex])/float(A[rowIndex][colIndex])
            ind = ind + 1
    factor[ind] = 
    for m in range(3):
        print(factor[m],end=' ')
    print()
    

#选择出基变量和入基变量并调整
def chooseRow(index):
    print("chooseRow")
    print(index)
    tem = array([0,0,0])
    isAllNegetive = 1
    #求解比值
    for i in range(numB):
        #print(i)
        if(A[i][index] <= 0):
            continue
            tem[i] = -1
        else:
            isAllNegetive = 0
            tem[i] = b[i]/A[i][index]
    if(isAllNegetive):
        print("问题存在无界解")
    else:
        min = 100000000
        minIndex = -1
        #找到最小的比值
        for i in range(numB):
            if(tem[i] > 0):
                if(tem[i] < min):
                    min = tem[i]
                    minIndex = i+1
        print(minIndex)
        for n in range(numB+numFB):
            if(dispositionB[n] == minIndex):
                dispositionB[index] = minIndex
                dispositionB[n] = 0
                updateA(index,minIndex-1)
        printMessage()
        
                

#计算判别数以及目标函数值
def caculate(index):
    print("caculate")
    chooseRow(index)

#判断迭代是否能够终止
def judge():
    flag = 0#设置flag用于判断判别数中是否存在0
    for i in range(numFB):
        if(j[i] > 0):#根据bland规则，找到最左边的非0判别数后进行下一次迭代
            caculate(i)#选择主列
            break
        elif(j[i] == 0):
            flag = 1
        else:
            continue
    if(flag == 1):
        print("存在无穷多解,其中一个最优解为:")
        print(ans)


if __name__ == '__main__':
    a = array([1,2,3])
    print(a)
    printMessage()
    judge()
    print(vdot(b,j))