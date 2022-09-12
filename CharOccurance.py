word="dhavalsaxena"

charCount={}

for i in word:
    if i in charCount:
        charCount[i]+=1
    else:
        charCount[i]=1
print(charCount)