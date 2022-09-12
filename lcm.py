small=12    
large=65 
maxNum=max(small,large)

while(True):
    if(maxNum %large==0 and maxNum%small==0):
        print(f"{maxNum} is a lcm")
        break
    maxNum+=1
   