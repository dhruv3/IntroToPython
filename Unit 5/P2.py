#
#
#
#
#

class Animal:
    def __init__(self, name, weight):
        self.weight = float(weight)
        self.name = name

    def jump(self):
        return self.name,"just jumped"

    def speak(self):
        return "Sound"


class Dog(Animal):
    def __init__(self, name, weight, breed):
        Animal.__init__(self, name, weight)
        self.breed = breed

    def speak(self):
        return "Bow-Wow"


#
#main
#

myDoge = Dog("Lisa", 12, "Lab")
s1 = myDoge.jump()
print("My dog,", s1)
s2 = myDoge.speak()
print("My dog says", s2)

