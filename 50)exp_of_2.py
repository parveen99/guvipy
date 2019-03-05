n=int(input())
flag=0
for i in range(1,n):
    if(2**i==n):
        flag=1
if(flag==1):
    print("yes")
else:
    print("no")
