N23=int(input())
temp=N23
rem=0
while(N23>0):
    r=N23%10
    rem=rem*10+r
    N23=N23//10
if(temp==rem):
    print("yes")
else:
    print("no")
