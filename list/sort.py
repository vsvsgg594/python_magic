# You are given a binary array arr[], 
# where each element is either 0 or 1. 
# Your task is to rearrange the array in increasing order in place 
# ithout using extra space). You do not need to return anything; simply modify the input array.

# Examples:

# Input: arr[] = [1, 0, 1, 1, 0]
# Output: [0, 0, 1, 1, 1]
# Explanation: After arranging the elements in increasing order, elements will be as 0 0 1 1 1.

def binary_sort(arr):
    n= len(arr)
    if n==0:
        return -1
    return  arr.sort()  
arr= [1, 0, 1, 1, 0]
ans=binary_sort(arr)
print(ans)
