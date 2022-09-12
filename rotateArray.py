# arr=[1,2,3,4,5]
# n=3
# for i in range(0,n):
#     # print(i)
#     first=arr[0]
#     for i in range(0,len(arr)-1):
#         arr[j]=arr[j+1]


# reverse order
# for i in range(len(arr)-1,-1,-1):
#     print(arr[i],end="")

# largest no in array
# max=arr[0]
# for i in range(0,len(arr)):
#     if(arr[i]>max):
#         max=arr[i]
# print(f"Maximum number is: {max}")

# # smallest num
# min=arr[0]
# for i in range(0,len(arr)):
#     if(arr[i]>min):
#         min=min
# print(f"Maximum number is: {min}")

# sorting in ascending order
arr=[5,4,3,2,1]
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        temp=arr[i]
        arr[i]=arr[j]
        arr[j]=temp
print(arr)   