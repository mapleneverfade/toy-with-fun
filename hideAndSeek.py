#-*-coding:utf8-*-
import tkinter
import random
import tkinter.messagebox
from PIL import Image, ImageTk
import types

class Joy(tkinter.Tk):
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title('Knock Knock Knock')
        self.imagepath = 'C:\\Users\\chenchangyu\\Desktop\\收藏图\\201808281150477723.gif'   #　gif 文件路径
        self.png = self.gif_to_png()   # 将 gif 转换成 png
        self.logo_cute_1 = tkinter.PhotoImage(file='C:\\Users\\chenchangyu\\Desktop\\收藏图\\1.png')
        self.logo_cute_2 = tkinter.PhotoImage(file='C:\\Users\\chenchangyu\\Desktop\\收藏图\\2.png')
        self.logo_shy = tkinter.PhotoImage(file='C:\\Users\\chenchangyu\\Desktop\\收藏图\\64ce8b5494eef01f942a3d98e1fe9925bc317d76.jpg')
        #self.label_gif = tkinter.Label(self.root, image= self.logo_cute_1)                                                  # 定义label,显式gif

        self.label_gif = tkinter.Label(self.root, image = self.png[0])                                                  # 定义label,显式gif

        self.image_shy = tkinter.Label(self.root, image = self.logo_shy)

        self.label_text = tkinter.Label(self.root, text='Hey beauty',font = "Helvetica 16 bold italic")                                        # 定义label,显式文本
        self.button_love = tkinter.Button(self.root, text='不要戳我', command=self.love, bg='white',relief=tkinter.FLAT,width=3,height=3)    # 定义button
        self.button_leave = tkinter.Button(self.root, text='有本事追我啊', bg="yellow", fg='black',relief=tkinter.FLAT, width=7, height=3)  # 定义button

        self.num_of_gif = 0
    def gif_to_png(self):
        '''
            gif to png
        '''
        img_list = []
        count = 0
        img = Image.open(self.imagepath)
        try:
            while True:
                current = img.tell()
                img_list.append(img.copy())  # 须拷贝, 否则对象会被覆盖
                img.seek(current+1)
        except EOFError as e:
            pass
        img_list = list(map(ImageTk.PhotoImage, img_list))
        return img_list

    def quit_window(self):    # 定义点击关掉窗口后操作事件(禁止)
        tkinter.messagebox.showinfo('要乖噢','小仙女，此路不通哦')

    def love(self):  # 定义点击后响应事件
        tkinter.messagebox.showinfo('Good Girl','今晚...见！')
        self.root.destroy()

    # 改变button位置
    def change_locate_of_button(self,button):  # 随机改变移动按钮的位置
        self.button_leave.place(x=random.randint(1, 230), y=random.randint(1, 205), width=100, height=25)

    def show_gif(self):
        length = len(self.png)
        if self.num_of_gif < length:
            self.label_gif.configure(image = self.png[self.num_of_gif % length])
            self.num_of_gif += 1

            self.label_gif.after(300, self.show_gif)
        else:
            self.num_of_gif = 0
            self.label_gif.configure(image = self.png[0])
            self.label_gif.after(300, self.show_gif)


    def run(self):
        self.root.geometry('400x270+800+400')
        i = 1
        self.label_gif.pack()
        self.label_gif.after(300, self.show_gif)
        self.image_shy.place(x= 285, y = 215)

        #self.label_text.pack()
        self.button_love.place(x= 340, y = 240,width =55, height=20)

        self.button_leave.bind('<Motion>', self.change_locate_of_button)  # 追踪鼠标位置，hide and seek
        self.button_leave.place(x=random.randint(1, 230), y=random.randint(1, 175), width=100, height=25)
        self.button_leave.focus_set()
        self.root.protocol('WM_DELETE_WINDOW', self.quit_window)
        self.root.mainloop()
if __name__=='__main__':
  main = Joy()
  main.run()
