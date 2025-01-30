# Write a Python code to display numbers from a list divisible by 5

def diviable_by_five(list):
    for i in range(0,len(list)):
        if list[i]%5==0:
            print(list[i])
ans=diviable_by_five([1,2,3,4,5,6,7,80,90,100,110,120,130]) 
print(ans)           


    