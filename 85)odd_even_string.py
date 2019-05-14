str56=input()
h7=""
h5=""
for i in range(0,len(str56)-1,2):
    h7=h7+str56[i]
for j in range(1,len(str56)-2,2):
    h5=h5+str56[j]
print(h7,h5)
