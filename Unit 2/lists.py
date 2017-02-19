### List

MyList = ['d', 'h', 'r', 'u', "v Dogra", 3]

print(MyList)
print(MyList[4])

MyList[4] = 'v'
print(MyList)

newList = ["test", MyList, 'error']
print(newList)

newList[1][1] = "I replaced u"
print(newList)

intList = [1, 2, 3, 4, 5]
print(sum(intList))
