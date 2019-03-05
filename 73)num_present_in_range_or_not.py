word2=int(input())
ju1,ju2=map(int,input().split())
flag=0
for i in range(ju1+1,ju2):
    if(i==word2):
        flag=1
        break
    else:
        flag=0
if(flag==1):
    print("yes")
elif(flag==0):
    print("no")
