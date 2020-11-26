from numpy import *

#目标函数系数矩阵
c = array([1,-3,-1])

#约束条件系数矩阵
A = array([[3.0,-1.0,2.0,1.0,0.0,0.0],
           [-2.0,4.0,0.0,0.0,1.0,0.0],
           [-4.0,3.0,8.0,0.0,0.0,1.0]])

#行列数
cols = 6
rows = 3
#出入基变量的列下标
nextInCol = 0
nextOutCol = 0

#行下标
nextRow = 0

#约束右端项
b = array([7.0,12.0,10.0])

#基变量位置
dispositionB = array([0,0,0,1,2,3])

#判别数向量
mJudge = array([-1.0,3.0,1.0,0.0,0.0,0.0])

#打印右端项
def mPrintB():
    for i in range(rows):
        print(b[i] ,end=' ')
    print()

#打印判别数向量
def mPrintJudge():
    for i in range(cols):
        print(mJudge[i],end=' ')
    print()

#打印约束条件系数矩阵
def mPrintA():
    for i in range(rows):
        for j in range(cols):
            print(A[i][j],end=' ')
        print()

#查找选择的行并返回行下标
def searchRow(ColNum):
    print("searchRow")
    flag = 0
    minIndex = -1
    min = 1000000
    for i in range(rows):
        if(A[i][ColNum] > 0):
            flag = 1
            tem = float(b[i])/A[i][ColNum]
            if(tem < min):
                min = tem
                minIndex = i
    return minIndex

#查找主列并返回主列下标
def searchCol():
    print("searchCol")
    for i in range(cols):
        if(mJudge[i] > 0):
            return i
    return -1

#更新矩阵
def update(Col,Row):
    print("update")
    temp = array([0.0,0.0,0.0])
    ind = 0
    divide = A[Row][Col]
    print(divide)
    #得到除数
    for i in range(rows):
        if(i == Row):
            continue
        else:
            temp[ind] = A[i][Col]/divide
            ind = ind + 1
    temp[ind] = mJudge[Col]/divide
    for i in range(cols):
        ind = 0#重置ind从0开始使用被除数
        if(dispositionB[i] > 0):
            continue
        for j in range(rows):
            if(j == Row):
                continue
            else:
                A[j][i] = A[j][i] - A[Row][i]*temp[ind]
                ind = ind + 1
        mJudge[i] = mJudge[i] - A[Row][i]*temp[ind]
    
    for i in range(cols):
        A[Row][i] = A[Row][i]/divide
    
    ind = 0
    for i in range(rows):
        if(i == Row):
            continue
        else:
            A[i][Col] = 0.0
            b[i] = b[i] - b[Row]*temp[ind]
            ind = ind + 1
    b[Row] = b[Row]/divide
    mJudge[Col] = 0.0

    print("*****the A is ******")
    mPrintA()
    print("*****the judge is ******")
    mPrintJudge()
    print("***** the b is ******")
    mPrintB()
            
    for i in range(3):
        print(temp[i],end=' ')
    print()

#进行下一次迭代
def next():
    print("next")
    #先查找主列
    nextInCol = searchCol()
    #查找主行
    nextRow = searchRow(nextInCol)
    if(nextRow < 0):
        return 1
    #交换
    for i in range(cols):
        if(dispositionB[i] == (nextRow+1)):
            dispositionB[nextInCol] = dispositionB[i]
            dispositionB[i] = 0
            break
    #重新计算系数矩阵以及判别数
    update(nextInCol,nextRow)

#求解
def mSolve():
    Flag = 0
    while(Flag == 0):
        Flag = 2
        for i in range(cols):
            if(mJudge[i] > 0):#存在大于0的判别数，继续迭代
                ret = next()
                if(ret == 1):
                    Flag = 3
                else:
                    Flag = 0
            elif(mJudge[i] == 0):
                if(dispositionB[i] == 0):
                    print("error")
                    Flag = 1
            else:
                continue
    if(Flag == 1):
        print("存在无穷多解")
    elif(Flag == 2):
        print("存在唯一最优化解")
    elif(Flag == 3):
        print("存在无界解")

if __name__ == '__main__':
    mSolve()
    print("finished")
    print("the result is:")
    print(dot(c,b))