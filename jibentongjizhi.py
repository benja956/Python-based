def getnum():
     nums = []
     numstr = input("请输入数字(回车退出)：")
     while numstr != "":
          nums.append(eval(numstr))
          numstr = input("请输入数字(回车退出)：")
     return nums


def ave(numbers):
     i = 0
     for i in numbers:
          i += i 
          aver = i / len(numbers)
     return aver

def dev(numbers,ave):
     sdev = 0.0
     for i in numbers:
          sdev += (i - ave)**2
          fangcha = (sdev / (len(numbers)-1))**0.5
          
     return fangcha

def median(numbers):
     sorted(numbers)
     size = len(numbers)
     if size % 2 == 0:
          med = (numbers[size//2-1]+numbers[size//2])/2
     else:
          med = numbers[size//2]
     return med
n = getnum()
m = ave(n)
print("平均值:{},方差:{:.2},中位数:{}.".format(m,dev(n,m),median(n)))
