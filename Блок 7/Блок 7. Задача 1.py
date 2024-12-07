import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Определим функцию и её производные
def f(x):
    return np.log(5 * x**3) - np.sin(6 * x)
def f_prime(x):
    return (15 / x) - 6 * np.cos(6 * x)
def f_double_prime(x):
    return -15 / x**2 + (-36) * np.sin(6 * x)

# Определим отрезок
x=np.linspace(0.01, 5, 100)  # Начало с 0.01 чтобы избежать ln(0)
y=f(x)

# 1. Вычисление первой и второй производной
y_prime=f_prime(x)
y_double_prime=f_double_prime(x)

# 2. Найдем наибольшее и наименьшее значение функции на отрезке
y_min=np.min(y)
y_max=np.max(y)
x_min=x[np.argmin(y)]
x_max=x[np.argmax(y)]

# 3. Уравнение касательной и нормали
x0=x_max
y0=f(x0)
f_prime_x0=f_prime(x0)

# Уравнение касательной: y = f(x0) + f'(x0)(x - x0)
def tangent_line(x):
    return y0 + f_prime_x0 * (x - x0)

# Уравнение нормали: y = f(x0) - (x - x0) / f'(x0)
def normal_line(x):
    return y0 - (x - x0)/f_prime_x0

# 4. Построим графики
plt.figure(figsize=(12, 12))

# График функции + График касательной и нормали
plt.subplot(2,2,1)
plt.plot(x,y, label='f(x)', color='blue')
plt.plot(x, tangent_line(x), label='Касательная', color='grey')
plt.plot(x, normal_line(x), label='Нормаль', color='purple')
plt.plot([x_min],[y_min], 'ro', label='min')
plt.plot([x_max],[y_max], 'go', label='max')
plt.xlabel('x')
plt.ylabel('y')
plt.title('График касательной и нормали')
plt.legend()
plt.grid()

# График первой производной
plt.subplot(2,2,2)
plt.plot(x,y_prime, label="f'(x)", color='orange')
plt.xlabel('x')
plt.ylabel("f'(x)")
plt.title('Первая производная')
plt.grid()

# График второй производной
plt.subplot(2,2,3)
plt.plot(x,y_double_prime, label="f''(x)", color='red')
plt.xlabel('x')
plt.ylabel("f''(x)")
plt.title('Вторая производная')
plt.grid()

# Определение точек касательного расслоения
x_points=np.array([1,2,3,4])  # избегаем x=0 из-за ln(0) и деления на 0
f_values=f(x_points)
f_prime_values=f_prime(x_points)

# Создание графика без точек касательного расслоения
plt.subplot(2,2,4)
plt.plot(x,y, label='f(x)', color='blue')
plt.plot([x_min],[y_min], 'ro', label='min')
plt.plot([x_max],[y_max], 'go', label='max')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Касательное расслоение')
plt.grid()
plt.ylim(y_min-1,y_max+1)
plt.xlim(x_min-0.2,x_max+0.2)

# Добавление графиков касательных точек
for x0 in x_points:
    y0=f(x0)
    slope=f_prime(x0)
    tangent_line= y0 + slope * (x - x0)
    plt.plot(x,tangent_line, linestyle=':', label=f'Касательная в x={x0:.0f}')
plt.legend()

# Отображение графиков
plt.tight_layout()
plt.show()

# 5. Найдем длину кривой через интеграл
def len(x):
    return np.sqrt(1+f_prime(x)**2)
len,err=quad(len,0.01,5)
print("Длина кривой на отрезке [0;5]: ",int(len))