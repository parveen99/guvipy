N235=int(input())
flag=1
for i in range(2,N235):
    if(N235%i==0):
        flag=0
if(flag==1):
    print("yes")
else:
    print("no")
