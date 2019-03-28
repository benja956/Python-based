#1
"""
n = input("请输入:")

print("{:->20,}".format(eval(n)))
"""
#2
"""
pyinstaller -i a.ico -F a.py
"""
#3
"""
import random
random.seed(123)

for i in range(10):
     
     

     print(random.randint(1,999),end=",")
"""
#4
"""
import turtle as t
t.right(30)
t.fd(200)
t.right(-60)
t.fd(200)
t.right(-120)
t.fd(200)
t.right(-60)
t.fd(200)
"""
#5
"""
a = [[1,2,3], [4,5,6], [7,8,9]]
b = [3,6,9]
s = 0
for c in a:
     for j in range(3):
          s += c[j]*b[j]
print(s)
"""
#6???????????????????????????????
names = ["命运", "寻梦"]
for name in names:
    fi = open(name+"-网络版.txt", "r", encoding="utf-8")
    fo = open(name+"-字符统计.txt", "w", encoding="utf-8")
    txt = fi.read()
    d = {}
    for c in txt:
        d[c] = d.get(c, 0) + 1
    del d['\n']
    ls = list(d.items())
    ls.sort(key=lambda x:x[1], reverse=True)
    for i in range(100):
        ls[i] = "{}:{}".format(ls[i][0], ls[i][1])
    fo.write(",".join(ls[:100]))
    fi.close()
    fo.close()


def getList(name):
    f = open(name+"-字符统计.txt", "r", encoding="utf-8")
    words = f.read().split(',')
    for i in range(len(words)):
        words[i] = words[i].split(':')[0]
    f.close()
    return words
def main():
    fo = open("相同字符.txt", "w")
    ls1 = getList("命运")
    ls2 = getList("寻梦")
    ls3 = []
    for c in ls1:
        if c in ls2:
            ls3.append(c)
    fo.write(",".join(ls3))
    fo.close()
main()
     
