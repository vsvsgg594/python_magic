# Accept a list of 5 float numbers as an input from the user

def add_float_number():
    l1=[]
    num=int(input("enter the size of list :"))
    for i in range(0,num):
        n=float(input('enter float numer'))
        l1.append(n)
    return l1
ans=add_float_number()
print(ans)


    
