a = int(input("в первый день"))
b = int(input("сколько километров"))
n = 1
while a < b:
    a = a + a*0.1
    n = n + 1
print(n, a)
