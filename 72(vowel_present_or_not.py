word=input()
flag=0
for i in word:
    if((i=="a" )or (i=="e") or (i=="i") or (i=="o")or ( i=="u")):
        flag=1 
    else:
        break
if(flag==1):
    print("yes")
elif(flag==0):
    print("no")
