"""h,w = eval(input()) # 请输入身高(m)和体重(kg)，逗号隔开
print("BMI是 {:.1f}".format(w /(h*h)))

w = eval(input())
print("{}".format(hex(w)))

"""
s = input() # 请输入一个由1和0组成的二进制数字串：
d = 0

for i in s:
    if i == str(1):
        d = d+2**(len(s)-1)
    if i == str(0):
        d = d
    s = s[1:]
print("转换成十进制数是：{}".format(d))
