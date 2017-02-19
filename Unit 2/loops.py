### Loops

MyList = [2, 4, 6 , "Dhruv", 8]
for i in MyList:
    print(i)
print("#######")

# default start index = 0 and increment = 1
for i in range(0, 10, 1):
    print(i)

# problem: 300 natural number with squares > 50000
count = 0
for i in range(1, 301, 1):
    if i**2 > 50000:
        count = count + 1

print("Numbers with squares > 50000 are", count)


# while loops
char = 'y'
while char == 'y':
    print("Looping")
    char = input("Do you want to loop:")
print("While loop ends")
