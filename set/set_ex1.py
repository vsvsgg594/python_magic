# Given an integer array arr[],
# print all distinct elements from this array. 
# The given array may contain duplicates and 
# the output should contain every element only once.

# Examples: 

# Input: arr[] = {12, 10, 9, 45, 2, 10, 10, 45}
# Output: {12, 10, 9, 45, 2}


# Input: arr[] = {1, 2, 3, 4, 5}
# Output: {1, 2, 3, 4, 5}


# Input: arr[] = {1, 1, 1, 1, 1}
# Output: {1}

def print_distinct(arr):
    myset=set(arr)
    return myset

arr=[1,2,3,4,5,6,7,7,78,8]
print(print_distinct(arr))  # Output: {1, 2, 3,
