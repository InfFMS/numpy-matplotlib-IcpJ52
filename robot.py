# Описание задачи:
# Робот начинает своё движение из точки (0,0) на координатной плоскости. Его маршрут задаётся массивом из 100 случайных значений, где:1 — движение вверх.2 — движение вниз.3 — движение вправо.4 — движение влево.
# Ваша задача:
# Сымитировать маршрут робота, используя случайные числа.
# Найти конечное положение робота.
# Построить путь робота на графике (соединяя все пройденные точки).
# Подсчитать, сколько шагов робот сделал в каждую сторону.
# Определить расстояние от начальной точки до конечной.
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button

X = 0
Y = 0

coords_x = [X]
coords_y = [Y]

Steps_Left = 0
Steps_Right = 0
Steps_Up = 0
Steps_Down = 0

directions = ["Up", "Down", "Right", "Left"]


def on_click(val):
    global Steps_Up, Steps_Left, Steps_Right, Steps_Down, X, Y
    direction = np.random.choice(directions)
    if direction == "Up":
        Steps_Up += 1
        Y += 1
        coords_x.append(X)
        coords_y.append(Y)
    if direction == "Down":
        Steps_Down += 1
        Y -= 1
        coords_x.append(X)
        coords_y.append(Y)
    if direction == "Left":
        Steps_Left += 1
        X -= 1
        coords_x.append(X)
        coords_y.append(Y)
    if direction == "Right":
        Steps_Right += 1
        X += 1
        coords_x.append(X)
        coords_y.append(Y)
    traectory.set_data(coords_x, coords_y)
    traectory_dot.set_data([X], [Y])
    fig.canvas.draw_idle()
    text_stats = (f"Шагов влево {Steps_Left}  "
                  f"Шагов вправо {Steps_Right}\n"
                  f"Шагов вниз {Steps_Down}   "
                  f"Шагов вверх {Steps_Up} \n"
                  f"Дистанция  {(coords_x[-1] * coords_x[-1] +
                                 coords_y[-1] * coords_y[-1]) ** 0.5:.3f}")
    stats_box.set_text(text_stats)


# Создали поле с осями
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.35)

circle = plt.Circle((0, 0), 0.5, color="red", label="Начало")
ax.add_patch(circle)

traectory, = ax.plot(coords_x, coords_y, lw=2)
traectory_dot, = ax.plot([X], [Y], marker="o", color="green")

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.grid(True)
ax.set_title("Поле для робота")
# Описание кнопки
axnext = fig.add_axes([0.7, 0.1, 0.25, 0.1])
bnext = Button(axnext, 'STEP!')
bnext.label.set_fontsize(12)
bnext.label.set_fontname("Times New Roman")

text_stats = (f"Шагов влево {Steps_Left}  "
              f"Шагов вправо {Steps_Right}\n"
              f"Шагов вниз {Steps_Down}   "
              f"Шагов вверх {Steps_Up} \n"
              f"Дистанция  ")
stats_ax = fig.add_axes([0.1, 0.1, 0.6, 0.1])  # Позиция для статистики [x, y, width, height]
stats_ax.axis('off')  # Скрываем оси
stats_box = stats_ax.text(0, 1, text_stats,
                          fontsize=10, verticalalignment='top')

bnext.on_clicked(on_click)

plt.show()
