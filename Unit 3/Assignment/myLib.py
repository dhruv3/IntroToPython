

def isHarshad(myNum):
    temp = myNum
    digiSum = 0
    while(myNum >= 1):
        digiSum = digiSum + myNum%10
        myNum = (int)(myNum/10)   
    if(temp%digiSum == 0):
        return True
    else:
        return False

def isSiete(myNum):
    myNum =(int)(myNum/10)
    tensDigit = myNum % 10
    if(tensDigit == 7):
        return True
    else:
        return False

Hodges = 14
        
