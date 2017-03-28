import mySearches

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


print("Searching for 78700")
print("Binary search returned index:", mySearches.bsearch(78700, intList))
print("Linear Search returned index:", mySearches.lsearch(78700, intList))

print("Searching for 3333")
print("Binary search returned index:", mySearches.bsearch(3333, intList))
print("Linear Search returned index:", mySearches.lsearch(3333, intList))

print("Searching for 1118")
print("Binary search returned index:", mySearches.bsearch(1118, intList))
print("Linear Search returned index:", mySearches.lsearch(1118, intList))
