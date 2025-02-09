"""
Задание 2

Решите квадратное уравнение
5x**2-10x-400=0 последовательно
присвоив переменным a, b, c значения


Обязательно примените f-строки
"""
import cmath  # Импортируем модуль для работы с комплексными числами, если корни окажутся комплексными

# Присваиваем коэффициенты квадратного уравнения переменным
a = 5
b = -10
c = -400

# Вычисляем дискриминант
discriminant = (b**2) - 4*(a*c)

# Выводим значение дискриминанта (для отладки или информации)
print(f"Дискриминант: {discriminant}")

# Находим корни уравнения
if discriminant >= 0:
    x1 = (-b - discriminant**0.5) / (2*a)
    x2 = (-b + discriminant**0.5) / (2*a)
else:
    x1 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    x2 = (-b + cmath.sqrt(discriminant)) / (2 * a)

# Выводим корни уравнения
print(f"Первый корень: {x1}")
print(f"Второй корень: {x2}")