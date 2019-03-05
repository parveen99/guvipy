n1=int(input())
r1=c1=0
while(n1>0):
    s=n1%10
    r1=r1+s
    c1=c1+1
    n1=n1//10
print(c1)
