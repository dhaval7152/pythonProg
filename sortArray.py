# #Initialize array     
nums = [5, 2, 8, 7, 1];     
temp = 0;    
     
#Displaying elements of original array    
print("Elements of original array: ");    
for i in range(0, len(nums)):    
    print(nums[i], end=" ");    
     
#Sort the array in ascending order    
def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp


nums=[4,2,23,1,3]
sort(nums)
print(nums)  
     
#Displaying elements of the array after sorting    
    
print("Elements of array sorted in ascending order: ");    
for i in range(0, len(nums)):    
    print(nums[i], end=" ");    



