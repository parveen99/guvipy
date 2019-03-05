mum2=input()
flag=0
for i in mum2:
    if((i=="0") or (i=="1")):
        pass
    else:
        flag=1 
        break
if(flag==0):
    print("yes")
elif(flag==1):
    print("no")
