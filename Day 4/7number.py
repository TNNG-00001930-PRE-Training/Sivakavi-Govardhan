'''7. Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.'''
def n(s,e):
    for i in range(s,e+1):
        if not any(digit in '13579' for digit in str(i)):
            print(i,end=",")
        else:
            pass
s=int(input("Enter the starting number: "))
e=int(input("Enter the ending number: "))
n(s,e)
