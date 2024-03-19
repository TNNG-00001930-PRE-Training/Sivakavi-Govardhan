def st(word):
    s=word.split()
    for i in s:
        if len(i)%2==0:
            print(i)
        else:
            pass
word=input()
st(word)
