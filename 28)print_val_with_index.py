N=int(input())
a=[]
a=[int(N) for N in input().split(" ")]
for i in range(0,len(a)):
    print(a[i],i)
