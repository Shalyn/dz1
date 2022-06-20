# Задание 2
time = int(input("vvedite vremya"))
print(f'Время в формате', time / 3600, time / 60, time / 1, sep=':')
chas = time / 3600
min = time / 60
print(f"Время в формате - {chas}:{min}:{time}" )
