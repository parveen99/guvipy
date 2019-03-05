n=int(input())
r=c=0
while(n>0):
    s=n%10
    r=r+s
    c=c+1
    n=n//10
print(c)
