a3=input()
c=0
b="[@_!#$%^&*()<>?/\|}{~:]"
k=[]
for i in b:
    k.append(i)
for i in a3:
    if i in k:
        c=c+1
print(c)
