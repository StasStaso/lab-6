# --------------------Завдання--------------------------
# Дано два вектори x,y.З’ясувати, чи паралельні вони.
# --------------------Рішення---------------------------
from functools import reduce

#                ---  Змінні  ---

x = list(map(int, input('Введіть х через пробіл(1 2 3 4): ').split()))
y = list(map(int, input('Введіть y через пробіл(1 2 3 4): ').split()))
result = sum(list(map(lambda a, b: a + b, x, y)))
print("\n")
#               ---  Обчислення ---
print("Перпендикулярні")if result == 0 else print("Неперпендикулярні")
