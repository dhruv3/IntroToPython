### String related programs

MyStr = "Say my name. Heisenberg. You're goddamn right!"

### length
print(len(MyStr))

### access chars
print(MyStr[5])
# range last char excluded
print(MyStr[1 : 5])

### string methods
print(MyStr.upper())
#strings are immutable
print(MyStr.replace("Heisenberg", "Dhruv"))

print(MyStr.count("y"))

#reverse indexing
newStr = "Hello World"
print(newStr[-4 : -1])
##below thing doesn't work as Python wants indexing from L to R
print(newStr[-1 : -4])
