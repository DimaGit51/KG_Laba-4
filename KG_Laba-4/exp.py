import tkinter as tk
import math
import numpy as np

# Уравнение поверхности "Чеснок"
def garlic_surface(a, b, R, K, A):
    x = R * math.sin(a) * math.cos(b) * (1 + 0.5 * abs(math.sin(K * b)))
    y = R * math.sin(a) * math.sin(b) * (1 + 0.5 * abs(math.sin(K * b)))
    z = -R * math.sqrt(A * (math.sin(0.5 * a))**1.5) + 1.5 * R
    return x, y, z

# Создание окна
root = tk.Tk()
root.title("3D Affine Transformations")

# Создание холста
canvas = tk.Canvas(root, width=600, height=600)
canvas.pack()

# Параметры уравнения поверхности
R = 1.0
A = 6.0
K = 4.0

# Масштаб
scale = 50

up_corner = 0

# Функция для отображения трехмерной точки на двумерный холст
def project_3d_to_2d(x, y, z):
    return x * scale + 300, -z * scale + 300

# Рисование трехмерной поверхности
for a in range(0, 360, 10):
    for b in range(0, 360, 10):
        rad_a = math.radians(a)
        rad_b = math.radians(b)
        x, y, z = garlic_surface(rad_a, rad_b, R, K, A)
        screen_x, screen_y = project_3d_to_2d(x, y, z)
        root.update()
        canvas.create_oval(screen_x, screen_y, screen_x + 2, screen_y + 2, fill="black")

# Применение аффинных преобразований к поверхности (примеры)

# Перемещение вдоль осей
def translate(x, y, z, dx, dy, dz):
    return x + dx, y + dy, z + dz

# Масштабирование
def scale_point(x, y, z, sx, sy, sz):
    return x * sx, y * sy, z * sz

# Вращение вокруг осей
def rotate_around_x(x, y, z, angle):
    rotation_matrix = np.array([[1, 0, 0],
                                [0, math.cos(angle), -math.sin(angle)],
                                [0, math.sin(angle), math.cos(angle)]])
    point = np.array([x, y, z])
    rotated_point = np.dot(rotation_matrix, point)
    return tuple(rotated_point)

# Применение аффинного преобразования к каждой точке поверхности
def post():
    transformed_points = []
    for a in range(0, 360, 10):
        for b in range(0, 360, 10):
            rad_a = math.radians(a)
            rad_b = math.radians(b)
            x, y, z = garlic_surface(rad_a, rad_b, R, K, A)
            # Примеры преобразований
            # x, y, z = translate(x, y, z, 3, 0, 0)  # Перемещение вдоль осей
            # x, y, z = scale_point(x, y, z, 0.5,0.5, 0.5)  # Масштабирование
            x, y, z = rotate_around_x(x, y, z, math.radians(up_corner))  # Вращение вокруг оси x
            transformed_points.append((x, y, z))
    canvas.delete('transform')
# Отображение преобразованных точек на холсте
    for point in transformed_points:
        x, y, z = point
        screen_x, screen_y = project_3d_to_2d(x, y, z)
        canvas.create_line(screen_x+200, screen_y+200, screen_x+200 + 2, screen_y+200 + 2, fill="red", tag='transform')


def Up(event):
    global up_corner
    up_corner+=1
    post()
    print(up_corner)
def Down(event):
    global up_corner
    up_corner-=1
    post()
    print(up_corner)
root.bind("<Up>", Up)
root.bind("<Down>", Down)

# Запуск окна
root.mainloop()
