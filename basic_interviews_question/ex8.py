# num=123
#output =321
def reverse_num(num):
    rev=0
    while num>0:
        r=num%10
        rev=rev*10+r
        num=num//10
    return rev    
print(reverse_num(12345))