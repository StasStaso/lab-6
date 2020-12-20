# -------------------Змінні------------------------

n = int(input('n= '))
a = [-4, 3]
b = int(input('b= '))
c = int(input('c= '))

#                ---Обчислення---

for i in range(2, n):
    a.append(a[i-1]**2 + 2 * a[i-2] - (i+1))


print(f"Середнє значення: {sum(a[b:c]) / len(a[b:c])}")
