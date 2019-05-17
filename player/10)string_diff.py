a12,b12=map(str,input().split(" "))
c=0
for i in a12:
    if i not in b12:
        c+=1
if(c==1):
    print("yes")
else:
    print("no")
