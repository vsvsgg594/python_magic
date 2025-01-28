# Given an integer k and array arr. Your task is to return 
# the position of the first occurrence of k in the given array 
# and if element k is not present in the array then return -1.

# Note: 1-based indexing is followed here.

# Examples:

# Input: k = 16 , arr = [9, 7, 16, 16, 4]
# Output: 3
# Explanation: The value 16 is found in the given array at positions 3 and 4,
#       with position 3 being the first occurrence.

def search(k, arr):
    n=len(arr)
    if n==0:
        return -1
    for i in range(0,n):
        if arr[i]==k:
            return i+1

arr=[1,2,3,4,5]
k=3
ans = search(k,arr)  
print(ans)      