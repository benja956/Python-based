#1
"""
s = input("请输入")
print("{:=^15}".format(s[0:15]))
"""
#2
"""
a,b = 0, 1
while a <=100:
    print(a, end = ",")
    a, b = b,a+b
"""
#3
"""
import time
timestr = "2020-10-10 10:10:10"
t = time.strptime(timestr, "%Y-%m-%d %H:%M:%S")
print(time.strftime("%Y年%m月%d日%H时%M分%S秒", t))
"""
#4
"""
import turtle as t
for i in range(3):
    t.seth(120*i)
    t.fd(200)
"""
#5
"""
d = {"数学":101, "语文":202, "英语":203, "物理":204, "生物":206}
d["化学"] = 205
d["数学"] = 201
del d["生物"]
for key in d:
     print("{}:{}".format(d[key],key))
"""
#6


import random
ls = []
first = ""
s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
while len(ls) < 10:
     pwd = ""
     for i in range(10):
          pwd += s[random.randint(0,len(s)-1)]
     if pwd[0] in first:
               continue
     else:
               ls.append(pwd)
               first += pwd[0]
fo = open("txt.txt","w",encoding = "utf-8")
fo.write(str("\n".join(ls)))
fo.close()
    

