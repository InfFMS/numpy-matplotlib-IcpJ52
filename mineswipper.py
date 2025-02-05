# Задача:
# Создайте игровое поле для "Сапёра" размером 10×10.
# Поле должно быть представлено в виде двумерного массива.
# Разместите 15 мин случайным образом (обозначьте их числом −1).
# Для каждой клетки без мины подсчитайте количество мин в соседних клетках.
# Визуализируйте:
# Само поле (где мины выделены красным).
# Поле с числами, где указано количество мин вокруг каждой клетки (для наглядности).
#
import numpy as np
import matplotlib.pyplot as plt

field = np.zeros((10, 10))
mines = np.random.choice(np.array([str(x) + ' ' + str(y) for x in range(10) for y in range(10)]), 15, replace=False)
for coord in mines:
    x, y = map(int, coord.split())
    field[y, x] = -1
for x in range(10):
    for y in range(10):
        if field[y, x] != -1:
            tmp = field[max(0, y - 1): min(y + 1, 9) + 1, max(0, x - 1): min(x + 1, 9) + 1]
            mines_around = np.count_nonzero(tmp == -1)
            field[y, x] = mines_around
fig, ax = plt.subplots()
for i in range(11):
    ax.plot([i, i], [0, 10], color='black')
for i in range(11):
    ax.plot([0, 10], [i, i], color='black')
for x in range(10):
    for y in range(10):
        if field[y, x] == -1:
            circle = plt.Circle((x + 0.5, y + 0.5), 0.1, color='red')
            ax.add_patch(circle)
        else:
            ax.text(x + 0.5, y + 0.5, str(int(field[y, x])), ha='center', va='center')
plt.axis('off')
plt.show()
