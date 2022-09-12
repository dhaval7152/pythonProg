prevNo=0
nextNo=1
sum=0
no=[]
for i in range(0,10):
    print(prevNo,",",end="")
    sum=prevNo+nextNo
    prevNo=nextNo
    nextNo=sum
# print(prevNo,",",end="")
print(no)