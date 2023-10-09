# Для построения графиков подключаем соответствующие библеотеки
import numpy as np
import matplotlib.pyplot as plt

# Создаем массив значений x от 0 до 2pi с шагом 0.01
x = np.arange(0, 2*np.pi, 0.01)

# Создаем массивы значений Y для каждого значения n
Y1 = np.sin(x)
Y2 = np.sin(2*x)
Y3 = np.sin(3*x)
Y4 = np.sin(4*x)

# Строим графики функций для каждого значения n
plt.plot(x, Y1, label='n=1')
plt.plot(x, Y2, label='n=2')
plt.plot(x, Y3, label='n=3')
plt.plot(x, Y4, label='n=4')

# Устанавливаем подпись оси x
plt.xlabel('x')

# Устанавливаем подпись оси y
plt.ylabel('y')

# Устанавливаем заголовок графика
plt.title('Графики функций y = sin n x')

# Отображаем легенду
plt.legend()

# Выводим график на экран
plt.show()

