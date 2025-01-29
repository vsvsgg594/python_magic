# Given two arrays a[] and b[], 
# the task is find intersection of the two arrays. 
# Intersection of two arrays is said to be elements that are common in both arrays.
# The intersection should not count duplicate elements and the result should contain items in any order.

# Input: a[] = {1, 2, 1, 3, 1},  b[] = {3, 1, 3, 4, 1}
# Output: {1,  3}

def intersection(arr1, arr2):
    first_set=set(arr1)
    second_set=set(arr2)
    return first_set & second_set
a = [1, 2, 1, 3, 1]

b= [3, 1, 3, 4, 1]
ans=intersection(a,b)
print(ans)