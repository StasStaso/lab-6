# --------------------Завдання--------------------------
# Перетворити масив таким чином, щоб спочатку
# розміщувались всі елементи, які мають непарні індекси,
# а потім з парними індексами.
# --------------------Рішення---------------------------

#                ---  Змінні  ---
array = list(map(int, input('Введіть елементи через пробіл(1 2 3 4): ').split()))
newArray = array[1::2]+array[::2]
#               ---  Вивід ---
print(newArray)



