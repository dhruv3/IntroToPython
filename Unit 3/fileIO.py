#
#File I/O stuff
#

#Method 1
infile = 'testTextFile.txt'

f = open(infile, 'r')
data = f.read()
f.close()

print(data)

#len gives total char in the string data
print(len(data))

#clean the data
data = data.replace('"', '')
dataList = data.split(', ')
print(dataList)
print(len(dataList))



#Method 2
with open("testNum.txt", "r") as f:
    for line in f:
        print(line)


#write to a file
of = open("newOPFile.txt", "w")

with open("testNum.txt", "r") as f:
    for line in f:
        tempStr = line;
        of.write(tempStr)

of.close()
#of we dont close we wont be able to write into our file
#this is because data we "wrote" stays in RAM and is only written to harddrive after file is closed

