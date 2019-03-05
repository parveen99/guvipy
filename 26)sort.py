N=int(input())
a=[]
a=[int(N) for N in input().split(" ")]
a.sort()
x=''
for i in range(0,len(a)):
    x=x+str(a[i])+' '
print(x)
