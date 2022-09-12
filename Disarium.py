# A number is said to be the Disarium number when the sum of its digit raised to the power of their respective positions becomes equal to the number itself.

# For example, 175 is a Disarium number as follows:

# 11+ 72 + 53 = 1+ 49 + 125 = 175
def numLen(num):
    len=0
    while(num!=0):
        len=len+1
        num=num//10
    return len
# num=135#squre_with_index=1+9+125=135

def disarium(num):
    rem=sum=0
    le=numLen(num)
   
    while(num>0):
        rem=num%10
        sum=sum+int(rem**le)
        num=num//10
        le=le-1
    return sum
   
# result=disarium(175)
# print(result)

for i in range(1,1000):
    result=0 
    result=disarium(i)
    if(result==i):
        print(f"{i} is disarium number")
    