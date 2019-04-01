#1
"""
inputstr = input("请输入：")
print("‘{}’字的Unicode编码：{}".formxt(str(inputstr),ord(str(inputstr))))
"""
#2
"""
m = eval(input("请输入第一个数："))
n = eval(input("请输入第二个数："))
def gcd(x,y):
     if x >= y:
         x,y = y,x
     while x % y != 0:
          r = x % y
          x = y
          y = r
     return y
print("{}和{}的最大公约数是{}".format(m,n,gcd(m,n)))
     
"""
#3
"""
s = 0
ls = eval(input("请输入"))
for i in ls:
     s += i
n = s/len(ls)
print(n)     
"""
#4
"""
import turtle
for i in range(4):
     turtle.right(90)
     turtle.circle(50,180)
"""

