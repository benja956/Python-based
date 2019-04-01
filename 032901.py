#1
"""
n = input()
nums = list(n.split(",")) 
s = 0
for i in nums:
    s += eval(i)
print(s)
"""
#2
"""
import jieba
s = "世界冠军运动员的乒乓球拍卖完了"
ls = jieba.lcut(s,True)
print(ls)
"""
#3
"""
import turtle as t
for i in range(4):
    t.seth(90+i*90)
    t.circle(200, 90)
    t.seth(270+i*90)#
    t.circle(200, 90)
  
"""
#4
"""
def is_prime(n):
     for i in range(2,n):
          if n % i == 0:
               return False
     return True

ls = [23,45,78,87,11,67,89,13,243,56,67,311,431,111,141]
for i in ls.copy():
    if is_prime(i)== False:
         ls.remove(i)
print(len(ls))   #此处为一行代码print(len(ls))
"""
#5


#读入CSV格式数据到列表中

fo = open("SunSign.csv","r", encoding='utf-8')
ls = []
for line in fo:
     line.replace("\n","")
     ls.append(line.split(","))
fo.close()
while True:
     strin = input("请输入")
     flag = False
     if strin == "exit":
          break
     for line in ls:
          if strin == line[0]:
               
               print("{}{}{}".format(chr(eval(line[3])),line[1],line[2]))
               flag = True
     if flag == False:
          print("failed to do")
