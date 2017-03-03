#
#driver
#

import palinTools

#file io
f = open('dataFile.txt', 'r')
data = f.read()
f.close()
#print(data)

#clean data
data = data.replace("\t", ",").replace("\n",",")
data = data.split(",")
#print(data)

#examine numbers
for i in data:
    if palinTools.isPalindrome(i):
        print (i)


