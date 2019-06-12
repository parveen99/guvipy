hu81,hu82=map(int,input().split(" "))
lon=hu82//hu81
for i in range(1,hu82):
    if(hu81%i==0 and hu82%i==0):
        c=i
print(c)
