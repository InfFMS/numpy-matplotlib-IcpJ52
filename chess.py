# Задача:
# Создайте шахматную доску размером 8×8, где чёрные клетки обозначены числом 1, а белые — 0.
# Укажите координаты клетки, где находится ферзь, например, [4,4].
# Определите клетки, которые атакует ферзь (в строке, столбце и диагоналях).
# Визуализация: Используйте тепловую карту (imshow), чтобы показать шахматную доску. Отметьте положение ферзя и атакуемые клетки цветами.
import numpy as np
import matplotlib.pyplot as plt

chess = [[i % 2 for i in range(j, 8 + j)] for j in range(8)]
arr_chess = np.array(chess, dtype=np.float64)
x, y = map(int, input('Введите координаты ферзя: ').split(','))
arr_chess[8 - y, :] = 0.2
arr_chess[:, x - 1] = 0.2
i = 0
while True:
    i += 1
    if x - 1 + i < 8 and 8 - y + i < 8:
        arr_chess[8 - y + i, x - 1 + i] = 0.2
    else:
        break
i = 0
while True:
    i -= 1
    if x - 1 + i >= 0 and 8 - y + i >= 0:
        arr_chess[8 - y + i, x - 1 + i] = 0.2
    else:
        break
i = 0
while True:
    i += 1
    if x - 1 + i < 8 and 8 - y - i >= 0:
        arr_chess[8 - y - i, x - 1 + i] = 0.2
    else:
        break
i = 0
while True:
    i += 1
    if x - 1 - i >= 0 and 8 - y + i < 8:
        arr_chess[8 - y + i, x - 1 - i] = 0.2
    else:
        break
arr_chess[8 - y, x - 1] = 0.5

plt.imshow(arr_chess, cmap='hot_r')
plt.xticks(ticks=range(0, 8), labels=list('ABCDEFGH'))
plt.yticks(ticks=range(7, -1, -1), labels=list('12345678'))
plt.show()
