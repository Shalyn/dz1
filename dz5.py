#Задание5
money = int(input("Vvedite viruchky:"))
izderjki = int(input("Vvedite izderjki:"))
prib = money - izderjki
rentab = izderjki / money
if money - izderjki > 0:
    print("Финансовый результат - прибыль. Ее величина:", prib)
    print("Рентабельность выручки = ", rentab)
    sotrud = int(input("Введите число сотрудников:"))
    print("Прибыль фирмы  расчете на одного сотрудника = ", prib / sotrud)
else:
    print("Финансовый результат - убыток. Ее величина: ", prib)

