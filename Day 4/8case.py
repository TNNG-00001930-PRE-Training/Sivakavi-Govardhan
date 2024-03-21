'''8. Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9'''
def cas(n):
    ucount=0
    lcount=0
    u="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    l="abcdefghijklmnopqrstuvwxyz"
    for i in n:
        if i in u:
            ucount+=1
        elif i in l:
            lcount+=1
        else:
            pass
    print("Upper letters ",ucount)
    print("Lower letters ",lcount)
n=input("Enter the string :")
cas(n)
