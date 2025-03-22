list_a = [10,90,90,98,89,90.89,8]
print("max() returns max value")
print(list_a)
print(max(list_a))
print("min() returns min value")
print(list_a)
print(min(list_a))

print("map() maps function to each items")
new_list = list(map(lambda x: x*2,list_a))
print(new_list)

char_list = ["milk","egg","pancake"]
new_char_list = list(map(lambda x: x+'s',char_list))
print(new_char_list)