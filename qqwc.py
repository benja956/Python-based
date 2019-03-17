#聊天词云生成器
import tkinter as tk
import wordcloud,jieba
import pkuseg
import matplotlib.pyplot as plt


window = tk.Tk()
window.title("聊天词云生成器v1.0")
window.geometry("400x400")

l1 = tk.Label(window,text="请输入txt文件的绝对路径：").place(x=0,y=0)

l2 = tk.Label(window,text="您选择的文件是：").place(x=0,y=90)

e = tk.Entry(window,show=None,width=30)

e.place(x=150,y=0)

def choose():
     t.delete(0.0,tk.END)
     ch = e.get()
     t.insert("insert",ch)

b1 = tk.Button(window, text="确认选择", width=15,
              height=2, command=choose)

b1.place(x=150,y=30)


t = tk.Text(window,bg="white",font = ("msyh",12),width=26,
             height=2)
t.place(x=150,y=90)

def wcloud():
     f = open(e.get(),"r",encoding="utf-8")
     t = f.read()
     f.close()
     seg = pkuseg.pkuseg()
     ls = seg.cut(t)
     txt = " ".join(ls)
     backgroud_Image = plt.imread('heart.gif')
     w = wordcloud.WordCloud( font_path = "msyh.ttc",
                         width = 1000,
                         height = 700,
                         background_color = "white",
                         max_words = 80,
                         mask = backgroud_Image)
     w.generate(txt)
     w.to_file("new.png")

b2 = tk.Button(window, text="开始执行", width=15,
              height=2, command=wcloud)

b2.place(x=150,y=150)
window.mainloop()
