# Given an array, arr of n integers, and an integer element x, 
# find whether element x is present in the array.
# Return the index of the first occurrence of x in the array, or -1 if it doesn't exist.

def search(arr, x):
    n=len(arr)
    if n==0:
        return -1
    for i in (0,n):
        if i==x:
            print(f'element has  index of {i}')
        
arr=[1, 2, 3, 4]
x=4
search(arr,x)                
    
