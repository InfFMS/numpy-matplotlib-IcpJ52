# Задача:
# Создайте массив из 365 случайных чисел, представляющих дневную температуру (например, от −10 до 35).
# Найдите:
# Среднюю температуру за год.
# Количество дней с температурой выше 25.
# Самую длинную последовательность дней, когда температура была ниже 0.
# Визуализируйте:
# Линейный график температуры по дням.
# Гистограмму распределения температуры.
# Подсветку "холодных" и "жарких" дней на линейном графике.
import numpy as np
import matplotlib.pyplot as plt

temp = np.random.randint(-10, 36, 365)
mean_temp = temp.mean()
days_high_temp = len(temp[temp > 25])
max_row = 0
cnt = 0
for tmp in temp:
    if tmp < 0:
        cnt += 1
    else:
        max_row = max(max_row, cnt)
        cnt = 0
print(mean_temp, days_high_temp, max_row, sep='\n')

days = np.arange(1, 366)
plt.subplot2grid((1, 2), (0, 0))
plt.plot(days, temp, color='black')
plt.xlabel('День')
plt.ylabel('Температура')
Xpoints = np.array([])
Ypoints = np.array([])
colors = np.array([])
for i in range(365):
    is_hot_or_cold = False
    if temp[i] > 25:
        color = 'red'
        is_hot_or_cold = True
    elif temp[i] < 0:
        color = 'blue'
        is_hot_or_cold = True
    if is_hot_or_cold:
        Xpoints = np.append(Xpoints, i)
        Ypoints = np.append(Ypoints, temp[i])
        colors = np.append(colors, color)
plt.scatter(Xpoints, Ypoints, color=colors)
unique_temp, cnt_days = np.unique(temp, return_counts=True)
plt.subplot2grid((1, 2), (0, 1))
plt.bar(unique_temp, cnt_days, color='green')
plt.xlabel('Температура')
plt.ylabel('Количество дней')
plt.tight_layout()
plt.show()
