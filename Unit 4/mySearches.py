#print("Doing Binary Search")
def bsearch(x, intList):
    low = 0
    high = len(intList) - 1
    cnt = 0

    while(low <= high):
        mIdx = (low+high)//2
        m = intList[mIdx]

        if(x == m):
            print("Counter is", cnt)
            return mIdx
        elif(x < m):
            cnt = cnt + 1
            high = mIdx - 1
        else:
            cnt = cnt + 1
            low = mIdx + 1
    
    return -1

#print("Index is", bsearch(7,[1,2,3,4,5,7]))

#print("Doing Linear Search")
def lsearch(a, intList):
    cnt = 0;
    for i in range(0, len(intList), 1):
        if(a == intList[i]):
            print("Counter is", cnt)
            return i
        cnt = cnt + 1
    print("Counter is", cnt)
    return -1

#print("Index is", lsearch(5,[1,2,3,4,5,7]))  
    
