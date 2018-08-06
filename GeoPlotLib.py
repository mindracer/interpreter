from tkinter import *           # 导入 Tkinter 库
import cv2 as cv

# 读取图像，支持 bmp、jpg、png、tiff 等常用格式
img = cv.imread("C:/Users/Mindracer/Pictures/Lena.jpg")
# 创建窗口并显示图像
cv.namedWindow("Image")
cv.imshow("Image", img)
root = Tk()                     # 创建窗口对象的背景色
                                # 创建两个列表
li     = ['C','python','php','html','SQL','java']
movie  = ['CSS','jQuery','Bootstrap']
listb  = Listbox(root)          #  创建两个列表组件
listb2 = Listbox(root)
for item in li:                 # 第一个小部件插入数据
    listb.insert(0,item)

for item in movie:              # 第二个小部件插入数据
    listb2.insert(0,item)

listb.pack(padx=5, pady=20, side=LEFT)                    # 将小部件放置到主窗口中
listb2.pack(padx=5, pady=20, side=LEFT)
def helloButton():
    print('hello button')


Button(root, text='exit', command=exit).pack(fill=X)

root.mainloop()                 # 进入消息循环

