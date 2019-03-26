#1
"""N = eval(input())
# N取值范围是0—100，整数
print("{}%@{}".format(N,round((N/5))*"=")) """

#2
"""s = "学而时习之,不亦说乎?有朋自远方来,不亦乐乎?人不知而不愠,不亦君子乎?"
n = 0  # 汉字个数
m = 0  # 标点符号个数
m = s.count(",")+s.count("?")
n = len(s) - m
print("字符数为{}，标点符号数为{}。".format(n, m))"""


#3
"""N =input("请输入一个整数：")
m = eval(N)
s = 0
for i in range(m,m+100):
     if i%2 == 1:
          
          s += i
print(s)"""

#4
"""import turtle as t
for i in range(6):
    t.fd(200)
    t.left(60)"""
#5
def getInput():
  e = input("请输入一个整数：")
  if type(eval((e))) == int:
       q = 5
  elif type(eval((e))) == str:
       getInput()
  
  else:
       getInput()
  return e  # 只能是单行代码
print(getInput())


