from tkinter import *
import PIL
from PIL import Image
import math
from tkinter import ttk

#Разрешение Рабочего Экрана
SCREEN_X = 1200
SCREEN_Y = 600




COUNT_CNV = 4
DISTANCE_CNV_X = SCREEN_X//COUNT_CNV
DISTANCE_CNV_Y = SCREEN_Y//COUNT_CNV

START_CNV_1 =  0*DISTANCE_CNV_X
START_CNV_2 =  1*DISTANCE_CNV_X

START_CNV_X_3 =  2*DISTANCE_CNV_X
START_CNV_Y_3 =  2*DISTANCE_CNV_Y

START_CNV_4 =  3*DISTANCE_CNV_X


#Масштабирование разрешения
SCALING_RESOLUTION = 4

#Размеры исходного изображения
IMG = PIL.Image.open("pic/img-1.png")
width, height = IMG.size
WIDTH_IMG = width//SCALING_RESOLUTION
HEIGHT_IMG = height//SCALING_RESOLUTION

DISTANCE = 10
#Изображение сверху в координатах (0, 0)
CNV_X_1 = 0
CNV_Y_1 = 0

#Изоб
CNV_X_2 = WIDTH_IMG+DISTANCE
CNV_Y_2 = 0

CNV_X_3 = 0
CNV_Y_3 = HEIGHT_IMG+DISTANCE

CNV_X_4 = WIDTH_IMG+DISTANCE
CNV_Y_4 = HEIGHT_IMG+DISTANCE



GrayImgPixels = []
GradientImg = []

root = Tk()
root.title("KG_Laba-4 | 6201-090301 Dvoryanchikov")
root.geometry(str(SCREEN_X)+'x'+str(SCREEN_Y))
root.resizable(False, False)

cnv = Canvas(bg="white", width=SCREEN_X, height=SCREEN_Y)
cnv.pack()

gradient_ = 50
def display():
    global gradient_
    gradient_ = int(entry.get())
    entry.delete(0, END)
    ImgGRADIENTtoBLACKiWHITE()

cnv.create_rectangle(880, 450, 1200, 450, outline="#004D40")
cnv.create_rectangle(880, 450, 880, 600, outline="#004D40")
entry = ttk.Entry()
entry.place(x=900, y=522)
btn = ttk.Button(text="Обработать!", command=display)
btn.place(x=1035, y=520)

def translationRGB(a, b ,c):
    return '#%02x%02x%02x' % (a, b, c)
def Сursor(event):
    x = event.x
    y = event.y
    cnv.delete("pixel-color")
    cnv.create_line(x,0,x,SCREEN_Y, fill="red", tag="pixel-color")
    cnv.create_line(0, y, SCREEN_X, y, fill="red", tag="pixel-color")
    # a, b, c = img_1.get(x, y)
    # cnv.create_rectangle(20, 250, 120, 270, fill=translationRGB(a, b, c), outline="#000000")
    cnv.create_text(75, 360, text="Координаты x: " + str(x) + " | y: " + str(y), fill="#00BFFF", tag="pixel-color")


img_1 = PhotoImage(file="pic/img-1.png")
img_1 = img_1.subsample(SCALING_RESOLUTION, SCALING_RESOLUTION)
cnv.create_image(CNV_X_1,CNV_Y_1, image=img_1, anchor="nw")
# cnv.create_image(START_CNV_2,0, image=img_1, anchor="nw")
# cnv.create_image(START_CNV_3,0, image=img_1, anchor="nw")
# cnv.create_image(START_CNV_4,0, image=img_1, anchor="nw")

# cnv.create_image(400,0, image=img, anchor="nw")
# img.put("red", to=(5, 5, 15, 15))

#R=G=B=0,3*R + 0,59*G + 0,11*B,
def translationGRAY(r, g ,b):
    return int(0.3*r+0.59*g+0.11*b)
def translationGrayIntToHex(n):
    return '#%02x%02x%02x' % (n, n, n)

def ImgRGBtoGRAY_function():
    cnv.delete("gray-picture")
    global GrayImgPixels
    GrayImgPixels = [[0] * WIDTH_IMG for i in range(HEIGHT_IMG)]
    for y in range(HEIGHT_IMG):
        if y%10 == 0:
            root.update()
        for x in range(WIDTH_IMG):
            r, g, b = img_1.get(x, y)
            i = x + CNV_X_2
            j = y + CNV_Y_2
            gray = translationGRAY(r, g, b)
            GrayImgPixels[y][x] = gray
            cnv.create_rectangle(i, j, i+1, j+1, fill=translationGrayIntToHex(gray), outline=translationGrayIntToHex(gray), tag="gray-picture")

def ImgGRAYtoOutlineSelection():
    cnv.delete("gradient-picture")
    global GradientImg
    GradientImg = [[0] * WIDTH_IMG for i in range(HEIGHT_IMG)]
    for y in range(HEIGHT_IMG):
        if y % 10 == 0:
            root.update()
        for x in range(WIDTH_IMG):
            i = x + CNV_X_3
            j = y + CNV_Y_3
            current = GrayImgPixels[y][x]
            up = 0
            right = 0
            if y < HEIGHT_IMG-1:
                up = GrayImgPixels[y+1][x]
            if x < WIDTH_IMG-1:
                right = GrayImgPixels[y][x+1]
            dx = (right - current)
            dy = (up-current)
            gradient = int(math.sqrt(dx**2 + dy**2))
            GradientImg[y][x] = gradient
            cnv.create_rectangle(x, j, x+1, j+1, fill=translationGrayIntToHex(gradient), outline=translationGrayIntToHex(gradient), tag="gradient-color")

def ImgGRADIENTtoBLACKiWHITE():
    cnv.delete("gradientBW-picture")
    for y in range(HEIGHT_IMG):
        if y % 10 == 0:
            root.update()
        for x in range(WIDTH_IMG):
            i = x + CNV_X_4
            j = y + CNV_Y_4
            gradient = GradientImg[y][x]
            color = 0
            if gradient > gradient_:
                color=255
            else:
                color = 0
            cnv.create_rectangle(i, j, i+1, j+1, fill=translationGrayIntToHex(color), outline=translationGrayIntToHex(color), tag="gradientBW-color")

# IncreaseContrast = [[0, -1, 0],
#                     [-1, 4, -1],
#                     [0, -1, 0]]
IncreaseContrast = [[-1, -1, -1],
                    [-1, 9, -1],
                    [-1, -1, -1]]
A = 0
B = 1
def IncreaseContrast_function():
    cnv.delete('ContrastBW-color')

    global GrayImgPixels
    g = [0 for i in range(WIDTH_IMG+2)]
    GrayImgPixels.insert(0, g)
    for y in range(1, HEIGHT_IMG):
        GrayImgPixels[y].insert(0, 0)
        GrayImgPixels[y].append(0)
    GrayImgPixels.append(g)
    print(GrayImgPixels)
    for y in range(1, HEIGHT_IMG-1):
        if y % 10 == 0:
            root.update()
        for x in range(1, WIDTH_IMG-1):
            i = x + CNV_X_4 + WIDTH_IMG+10
            j = y
            C = A + B*((IncreaseContrast[0][0]*GrayImgPixels[y - 1][x - 1]) + \
            (IncreaseContrast[0][1]*GrayImgPixels[y - 1][x]) + \
            (IncreaseContrast[0][2]*GrayImgPixels[y - 1][x + 1]) + \
            (IncreaseContrast[1][0] * GrayImgPixels[y][x - 1]) + \
            (IncreaseContrast[1][1] * GrayImgPixels[y][x]) + \
            (IncreaseContrast[1][2] * GrayImgPixels[y][x + 1]) + \
            (IncreaseContrast[2][0]*GrayImgPixels[y + 1][x - 1]) + \
            (IncreaseContrast[2][1]*GrayImgPixels[y + 1][x]) + \
            (IncreaseContrast[2][2]*GrayImgPixels[y + 1][x + 1]))
            if C<0:
                C = 0
            elif C > 255:
                C = 255
            cnv.create_rectangle(i, j, i+1, j+1, fill=translationGrayIntToHex(C), outline=translationGrayIntToHex(C), tag="ContrastBW-color")
            root.bind("<B1-Motion>", Сursor)

btn_gray = ttk.Button(text="Перевод в черное-белое изображение", command=ImgRGBtoGRAY_function)
btn_gray.place(x=900, y=460)

btn_ImgGRAYtoOutlineSelection = ttk.Button(text="Градиентный метод func1", command=ImgGRAYtoOutlineSelection)
btn_ImgGRAYtoOutlineSelection.place(x=900, y=490)

btn_ImgGRAYtoOutlineSelection = ttk.Button(text="Контрастирование", command=IncreaseContrast_function)
btn_ImgGRAYtoOutlineSelection.place(x=900, y=550)

root.bind("<B3-Motion>", IncreaseContrast_function)
root.mainloop()