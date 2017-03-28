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
intList.sort()
