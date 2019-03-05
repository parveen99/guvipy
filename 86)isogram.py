a45=input()
flag=1
for i in a45:
    if(a45.count(i)>1):
        flag=0

if(flag==1):
    print("yes")
elif(flag==0):
    print("no")
