# filter

list_a = []
n = int(input("Enter Range: "))
for i in range(1,n):
    list_a.append(i)
    
even = list(filter(lambda x : x%2 == 0,list_a))
print(f"The Even numbers upto {n} are :",even)

print("Float() prints with decimal")
a = int(input("Enter Integer: "))
print(float(a))



