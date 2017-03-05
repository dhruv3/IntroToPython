import myLib

f = open('Rumbers.txt', 'r')
data = f.read()
f.close()

#clean data
data = data.replace('\t',',').replace('\n',',')
data = data.split(',')

#to stuff
harshadSum = 0
sieteHodgeList = []
harshadSieteList = []
hodgeList = []

for i in data:
    if(myLib.isHarshad((int)(i))):
       harshadSum = harshadSum + (int)(i)
       if(myLib.isSiete((int)(i))):
           harshadSieteList.append(i)
           if(int(i)%myLib.Hodges == 0):
                sieteHodgeList.append((int)(i))

print("Harshad sum is", harshadSum)
print("Siete numbers and hodge numbers")
print(sieteHodgeList)

newFile = open('HarshOut.txt', 'w')
for i in harshadSieteList:
    newFile.write(i)
    newFile.write("\n")
newFile.close()
