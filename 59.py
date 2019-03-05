n55=int(input())
r=c=0
while(n55>0):
    s=n55%10
    r=r+s
    c=c+1
    n55=n55//10
print(c)
