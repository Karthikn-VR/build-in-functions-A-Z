print("Eval() ")
a = input("Enter a expression: eg a + b: ")
print(eval(a))

source = """

a: int = 10
b: int = 20


"""
print(exec(source))
