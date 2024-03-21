'''4. Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters'''
class st:
    def __init__(self):
        self.a=""
    def getstring(self):
        self.a=input("Enter the string :")
    def printstring(self):
        print(self.a.upper())
s=st()
s.getstring()
s.printstring()