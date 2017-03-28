'''
Assignment_1:
The built in Python function pow(x,y) returns the number x to the power of y.  Write your own function that performs this task recursively.

Name it myPow() and have it accept two integers as arguments.  You do not have to handle a power less than 1 (myPow(64,.5) for example.  
Test it with myPow(7,3), myPow(2,6) and one example of your choosing.

(Hint: think about what exponentiation really is and consult the multiplication example we look at in the slides.  This should not be hard.) 
'''

def myPow(n, power):
    if(power == 0):
        return 1;
    return n*myPow(n, power-1)

print(myPow(3,3))
