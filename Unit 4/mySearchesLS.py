def bsearch(x, intList):
    low = 0
    high = len(intList) - 1
    cnt = 0

    while(low <= high):
        mIdx = int((low+high)/2)
        m = intList[mIdx]

        if(x == m):
            print(cnt)
            return mIdx
        elif(x < m):
            cnt = cnt + 1
            high = mIdx
        else:
            cnt = cnt + 1
            low = mIdx
    
    return -1

print(bsearch(7,[1,2,3,4,5,7]))
    
