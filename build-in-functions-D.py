# # dictonary

d = {
    1:{
        "name":"value"
    }
}
print(type(d))
print(d)

#list

d = [
    {
        "name":"value"
    }
]
print(type(d))
print(d)
d.append({"karthi":"20"})
print(d)

print("dir() Prints the file in scope: ")
print(dir())

print("divmod() prints the no. of times and remainder:\nTry yourself")
a = int(input("Enter number to be divided: "))
b = int(input("Enter divider: "))
print(divmod(a,b))