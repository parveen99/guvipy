N=int(input())
a=[]
a=[int(N) for N in input().split(" ")]
a.sort()
x=len(a)//2

print(a[x])
