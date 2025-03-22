def greet(name:str):
    print(f"Hello {name}")
    
name = input("Enter your Name: ")   
greet(name)

print("The function is callable so prints True")
print(callable(greet))  
print("The name is not callable so prints False")
print(callable(name))   

print("The chr() is used to print the respective character for value: ")

print("For 65: ",chr(65))

char = int(input("Try Yourself Enter a value: "))
print(chr(char))

print("complex values")
n1 = int(input("Enter a value: "))
n2 = int(input("Enter a value: "))
print(complex(n1,n2))