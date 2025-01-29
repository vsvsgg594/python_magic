# Given an array of integers arr[],
# The task is to find the index of first repeating element in it 
# i.e. the element that occurs more than once and whose index of the first occurrence is the smallest. 

# Examples: 

# Input: arr[] = {10, 5, 3, 4, 3, 5, 6}
# Output: 5 
# Explanation: 5 is the first element that repeats
def first_repeating_element(arr):
    s1=set()
    for i in range(0,len(arr)):
        if arr[i] in s1:
            return arr[i]
        else:
            s1.add(arr[i])
    return None        


arr=[1,2,3,4,5,6,7,8,5,3]
ans=first_repeating_element(arr)
print(ans)



