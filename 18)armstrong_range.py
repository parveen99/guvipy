x4,x5=map(int,input().split())
for i in range(x4,x5):
    temp=i
    s=0
    while(i>0):
        r=i%10
        s=s+r*r*r
        i=i//10
    if(temp==s):
        print(s,end=" ")
