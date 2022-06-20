#Задание4
x = int(input("Введите число"))
r = 0

while (x):
    if (x % 10 > r):
        r = x % 10
    x //= 10
print(r)