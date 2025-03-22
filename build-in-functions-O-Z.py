#ord
print("Prints the unicode of the character")
n = input("Enter the character: ")
print(f"unicode of {n} is: ",ord(n))

# #power
print("Pow() gives the power of integer")
a = int(input("Enter the Number: "))
b = int(input("Enter the Power: "))
print("The value is: ",pow(a,b))

#print

list_a = [10,20,30,34,40]
print("Print statemts")
print(list_a)
print(*list_a,sep=' - ')
print(*list_a,sep='||')
char_list = ['A', 'B', 'C', 'D', 'E']

print(*char_list, sep='-')
new = "\n".join(char_list)
print(new)

# #range
k = int(input("Enter range: "))
for i in range(1,k+1):
    print(i)


#round

float_num = 156.86444754240
print(round(float_num,1))
print(round(float_num,2))
print(round(float_num,3))
print(round(float_num,4))

for i in range(0,9):
    print(round(float_num,i))
    
#sorted
char_list_2 = ['z', 'u', 'o', 'l', 'j']
print(sorted(char_list_2))
char_list_3 = sorted(char_list_2,reverse=True)
print(char_list_3)

list_4 = [3,7,9,6,5,9,0]
print(sorted(list_4))
list_5 = sorted(list_4,reverse=True)
print(list_5)

# #SUM()

print("sum() prints the sum of items: ")
print("The sum of previous list is ",sum(list_4))

#yield
def count_up(n):
    for i in range(1, n + 1):
        yield i

gen = count_up(5)

for num in gen:
    print(num, end=" ")
    
#zip
print("The zip() combines ")
m = (1,3,5,7,8)
n = (0,9,7,6,5)
result = [a + b for a, b in zip(m, n)]
print(result)
print(list(zip(m,n)))
result2 = sum(map(sum, zip(m, n)))
print(result2)

# result = list(map(lambda a, b: a + b, m, n))