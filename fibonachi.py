import math

def fibonachchi(r):
    count=0
    a=1
    b=1
    out=1
    while (count!=r-1):
        print(out)
        a,b=b,out
        out=a+b
        count+=1
    print(str(r)+"element is"+str(out))


