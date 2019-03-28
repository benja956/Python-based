#1
"""
n = input("请输入")
nums = list(n.split(",")) 
s = 0
for i in nums:
     s += eval(i)
print(s)
"""
#2
def GreatCommonDivisor(a,b):
    if a > b:
        a,b = b,a
    r = 1
    while r != 0:
        r = a % b
        a = b
        b = r
        print(r,a,b)
    return a
m = eval(input("w"))
n = eval(input("w"))
print(GreatCommonDivisor(m,n))
