def me(s,e):
    for i in range(s,e+1):
        if (i%7==0 and i%5!=0):
            print(i,end=",")
        else:
            pass
s=int(input("Enter First number: "))
e=int(input("Enter the second number: "))
me(s,e)
