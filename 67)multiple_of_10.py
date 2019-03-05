
N99=int(input())
for i in range(0,9):
    if(N99%10==0):
        save=N99
        break
    else:
        N99=N99+1 
print(save)
