l1=[1,2,3,4,5]
print(l1)
l2=l1
print(l2)
# l2[2]=100
# print(l2)
l2=[1,2,3,4,5]
print(l1==l2)
print(l1 is l2)

l1.append(333)
print(l1)
l1.insert(1,1000)
print(l1)
l1.extend([1,2,3,4,4,5,6,6,7,78,8,98,9,])
print(l1)
print(l1.pop())
if 0 in l1:
    l1.remove(3)
else:
    print("item is not present in list")    
print(l1)

print(l1[::-1])