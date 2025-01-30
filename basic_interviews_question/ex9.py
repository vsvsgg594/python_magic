#num=123
#output 6
def sum_of_digit(num):
    sum=0
    while num>0:
        rem=num%10
        sum=sum+rem
        num=num//10
    return sum
print(sum_of_digit(123))
    