
arr = []
def getC():
    print('please input the col and row')
    col = int(input())
    row = int(input())
    f = open('data.txt')
    myData = f.read()
    print(type(myData))
    return
    ind = 0
    for i in range(row):
        for j in range(col):
            if((myData[ind] >= 48) & (myData[ind] <=57)):
                arr[i][j] = myData[ind] - '0'
            ind = ind + 1
    print(myData)
    for i in range(row):
        for j in range(col):
            print(arr[i][j],end=' ')

if __name__ == '__main__':
    getC()