import tkinter as tk
window = tk.Tk()
window.title("聊天词云生成器v1.0")
window.geometry("400x400")
"""
var = tk.StringVar()
l1 = tk.Label(window,textvariable="请输入txt文件的绝对路径：",font = ("Arial",12),width=15,
             height=2)
l1.pack(left)



on_hit = False
def hitme():
     global on_hit
     if on_hit == False:
          on_hit = True
          var.set("youhitme")
     else:
          on_hit = False
          var.set("")
"""
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


window.mainloop()
