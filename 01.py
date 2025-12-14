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

x = "bahar zand"
print(x.capitalize())

y = "bahar zand"
print(y.title())

z = "bahar zand"
print(z.upper())

m = "BAHAR ZAND"
print(m.casefold())

n = "BAHAR ZAND"
print(n.lower())

s = "bahar bahar zand"
print(s.count("bahar"))

e = "bahar zand"
print(e.find(z))

r = "my name is {} ."
print(r.format("bahar"))

t = "        bahar  zand             "
print(t.strip())

k = "bahar zand"
print(k.center(20 , "_"))


o = "bahar\tzand"
print(o.expandtabs(20))

h = "bahar zand"
print(h.replace("bahar" , "zahra"))
