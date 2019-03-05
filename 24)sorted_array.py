N=int(input())
a=[]
a=[int(N) for N in input().split(" ")]
a.sort()
for i in range(0,len(a)):
    print(a[i],end=" ")
