# Returns the absolute value 
n = int(input("Enter negative value: "))
print(abs(n))

# a  = int(input("Enter point1 value: ")) 
# b = int(input("Enter point2 value: "))

a = -7
b = 8

difference = abs(a - b)
print("Distance is \n",difference)

print(abs(7+4j))
print(abs(3+5j))
print(abs(2+6j))

list_a = [1,1,1,0,1]
list_b = [0,0,0,0,0]
list_c = [1,1,1,1]

print("All() returns only all the items are true\n")
print(all(list_a))
print(all(list_b))
print(all(list_c))
print("Any() returns if any of the items are true\n")
print(any(list_a))
print(any(list_b))
print(any(list_c))

char = "é"
print("é Ascii value is: ",ascii(char))

