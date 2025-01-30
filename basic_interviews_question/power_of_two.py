def find_power(num1,num2):
    if num2==0:
        return 1
    elif num2==1:
        return num1
    else:
        return num1**num2

ans=find_power(2,5)  
print(ans)  
    