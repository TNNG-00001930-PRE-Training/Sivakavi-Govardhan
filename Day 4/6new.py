'''6. Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
'''
def new(n):
    s=n.split(" ")
    se=set(s)
    l=list(se)
    t=sorted(l)
    k=" ".join(t)
    print(k)
n=input("Enter the sentance: ")
new(n)