# print.py_01
# Beginner python exercise _ printing text

print("hello world")

x = 5
y = 3
print(x+y)
print(x-y)
print(x*y)
print(x**y)
print(x/y)
print(x//y)
print(x%y)

x = "hello'world'"
print(x)
     
y = "hello\"nworld\""
print(y)

x = "hello\nworld"
print(x)

y = "hello\tworld"
print(y)

z = "hello\bworld"
print(z)

x = """hello world
my name is   \"bahar\" """
print(x)

x = "hello world"
print(x[1:-2])

name = "bahar"
lastname = "zand"
age = 18
x = f"hello my name is {name} and my last name is {lastname} i am {age} years old"
print(x)

x = "bahar"
print(x.capitalize())

y = "bahar"
print(y.upper())

z = "BAHAR"
print(z.casefold())
