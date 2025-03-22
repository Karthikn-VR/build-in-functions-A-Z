#id()
print("prints memory location: ")
a = 7
b = 8
c = 7
print(id(a))#same as c
print(id(b))# different
print(id(c))# same as a

list_a = [1,2,3,4]
list_b = [1,2,3,4]

print(id(list_a))# different
print(id(list_b))#different

# isistance()
print("isistance() checks for datatype")

print("Try")
a = input("ENTER: ")
if a.isdigit():  # Checks numbers
    a = int(a)
    print(isinstance(a,int))
    print("ok")
else:
    print("not an integer")    

print("iter() used to iterate through list or tuples")

list_c = [1,4,7,8]
my_iter = iter(list_c)
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(list_c)
for i in list_c:
    print(next(my_iter))