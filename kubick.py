# Задача:
# Смоделируйте 1000 бросков игрального кубика.
# Найдите:
# Сколько раз выпадало каждое значение (от 1 до 6).
# Вероятность выпадения каждого значения.
# Максимальное количество подряд выпавших одинаковых значений.
# Визуализируйте результаты в виде гистограммы.
import numpy as np
import matplotlib.pyplot as plt

result = np.random.randint(1, 7, 1000)
categories, values = np.unique(result, return_counts=True)
chances = values / 10
elem = result[0]
cnt = 0
max_cnt = [0] * 6
for el in result:
    if el == elem:
        cnt += 1
    else:
        max_cnt[elem - 1] = max(max_cnt[elem - 1], cnt)
        elem = el
        cnt = 1
plt.subplot2grid((2, 2), (0, 0))
plt.bar(categories, values, color='purple')
plt.xlabel('Результат броска')
plt.ylabel('Количество выпадений')
# plt.show()
plt.subplot2grid((2, 2), (1, 0))
plt.bar(categories, chances, color='red')
plt.xlabel('Результат броска')
plt.ylabel('Вероятность выпадения, %')
# plt.show()
plt.subplot2grid((2, 2), (0, 1), rowspan=2)
plt.bar(categories, max_cnt, color='green')
plt.xlabel('Результат броска')
plt.ylabel('Максимальное количество подряд выпавших одинаковых значений')
plt.show()
