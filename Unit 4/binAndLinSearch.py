

bsCount = 0

def bsMainFn(a, intList, low, high):
    global bsCount
    if(low > high):
        bsCount+= 1
        print(bsCount)
        return -1

    mIdx = (low+high)//2
    m = intList[mIdx]
    
    if(a == m):
        bsCount+= 1
        print(bsCount)
        return mIdx
    elif(a > m):
        bsCount+=1
        low = mIdx + 1
        return bsMainFn(a, intList, low, high)
    else:
        bsCount+= 1
        high = mIdx - 1
        return bsMainFn(a, intList, low, high)

def bsearch(a, intList):
    low = 0
    high = len(intList) - 1
    return bsMainFn(a, intList, low, high)

print(bsearch(7,[1,2,3,4,5,7]))

def linearSearch(a, intList):
    cnt = 0;
    for i in range(0, len(intList), 1):
        if(a == intList[i]):
            print(cnt)
            return i
        cnt = cnt + 1
    print(cnt)
    return -1

print(linearSearch(5,[1,2,3,4,5,7]))        



    
    
    
