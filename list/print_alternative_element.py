# You are given an array arr[], the task is to return 
# a list elements of arr in alternate order (starting from index 0).

# Examples:

# Input: arr[] = [1, 2, 3, 4]
# Output: 1 3
# Explanation:
# Take first element: 1
# Skip second element: 2
# Take third element: 3
# Skip fourth element: 4
def getAlternates(arr):
    n=len(arr)
    if n==0:
        return -1
    li=[]
    for i in range(0,n,2):
        li.append(arr[i])
    return li
ans=getAlternates([1,2,3,4])
print(ans)    
