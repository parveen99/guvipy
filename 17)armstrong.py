
n23=int(input())
temp=n23
s=0
while(n23>0):
    r=n23%10
    s=s+r*r*r
    n23=n23//10
if(temp==s):
    print("yes")
else:
    print("no")
