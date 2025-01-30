def find_factorail():
    n=int(input("enter the number for factorial"))
    if n<0:
        print("please enter the valid number ")
    elif n==0 or n==1:
        print(1) 
    ans=1    
    for i in range(1,n+1):
        ans=ans*i
    return ans       
ans=find_factorail()
print(ans)