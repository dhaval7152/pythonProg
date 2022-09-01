# Problem Definition
# Find the missing numbers in a given list or array using Python.

# For example in the arr = [1,2,4,5] the integer '3' is the missing number.

# There are multiple ways to solve this problem using Python. In this article, we will cover the most straightforward ones.

# Algorithm
# Step 1: Create an empty array for missing items

# Step 2: Loop over the elements within the range of the first and last element of the array

# Step 3: Compare the loop variable with the given array if the value is not present append it to the missing array

# Note: The array must be sorted for this to work. Use arr.sort() on an unsorted array before feeding it to the program.
# Solution 1

arr = [1,2,4,5,7,8]
missing_elements = []
for value in range(arr[0],arr[-1]+1):
    if value not in arr:
        missing_elements.append(value)
print(missing_elements)


