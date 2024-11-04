immutable_var = ("a", "b", 1, 2)
print(immutable_var)
#immutable_var[0] = 3
#print(immutable_var)
#TypeError: 'tuple' object does not support item assignment
mutable_list = [1,2,3]
print(mutable_list)
mutable_list[0] = 3
print(mutable_list)
