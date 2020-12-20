# --------------------Завдання--------------------------
# Дано одновимірний масив, який містить n дійсних чисел.
# З’ясувати, скільки серед елементів цієї послідовності
# є пар з трьох елементів, які слідують підряд і утворюють
# арифметичну прогресію.
# --------------------Рішення---------------------------

#                  ---Змінні---

while True:
    lenOfArray = int(input("К-ть елементів масиву(>=3): "))
    if lenOfArray >= 3:
        break
    else:
        print("Введіть к-ть елементів >3\n")
array = [int(input(f"Element[{i+1}] : ")) for i in range(lenOfArray)]
countOfSequence = 0

#                ---Обчислення---

for i in range(2, lenOfArray):
    if array[i] - array[i - 1] == array[i - 1] - array[i - 2]:
        countOfSequence += 1
print("К-ть прогресій з 3-х елементів: {countOfSequence}")
