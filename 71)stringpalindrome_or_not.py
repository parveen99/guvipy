word=input()
length_=len(word)
for i in range(0,(length_//2)+1):
    if(word[i]==word[(length_-1)-i]):
        i=i+1 
    else:
        break
if(i>length_/2):
    print("yes")
else:
    print("no")
