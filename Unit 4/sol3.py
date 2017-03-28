import matplotlib.pyplot as plt

infile = 'rands.txt'

f = open(infile, 'r')
data = f.read()
f.close()

#clean the data
data = data.replace('\n', '\t').replace('\t', ', ')
dataList = data.split(', ')

intList=[]
for i in dataList:
    intList.append((int)(i))

index =[]
for i in range(1, len(intList) + 1, 1):
    index.append(i)

plt.plot(index, intList)
plt.show()

intList.sort()
plt.plot(index, intList)
plt.show()
