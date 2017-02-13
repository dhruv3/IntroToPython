age = 10
weight = 60

user_age = int(input("Enter age"))
user_weight = int(input("Enter weight"))

if (age > user_age & weight > user_weight):
    print("Both less")
    
elif (age < user_age & weight < user_weight):
    print("Both greater")
    
else:
    print("Game Over.")
