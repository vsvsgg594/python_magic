
def find_power_number(num,n):
   

    if n==0:
        return 1
    elif n==1:
        return num
    else:
        return num**n
num=int(input('enter the number : '))

n=int(input('enter power number '))    
ans=find_power_number(num ,n)
print(ans)

        