d={1:"virat kohli",2:"darshana"}
print(d)
# create dictionary using dict() constructor
d2 = dict(a = "Geeks", b = "for", c = "Geeks")
print(d2)

# Accessing Dictionary Items
# We can access a value from a dictionary by using the key within square brackets orget()method.
# print(d[1])
# print(d.get(1))

# for i in d.values():
#     print(i)

for key,value in d.items():
    print(f'key is {key} and values is {value}')
    