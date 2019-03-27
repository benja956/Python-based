#1
"""
def getInput():
    try:
        txt = input("请输入整数：")   # "请输入整数: "
        while eval(txt) != int(txt):
            q = 1   # "请输入整数: "
    except:
        return getInput()
    return eval(txt)
print(getInput())"""

#2 tianlong
"""tj = {}
txt = open("E:\\bd\\caozuo\\stu\\do\\2\\天龙八部-网络版.txt","r")
t = txt.read
for word in t:
     count = count(word,0) + 1
     
     tj.append(count)"""

"""

fi = open("E:\\bd\\caozuo\\stu\\do\\2\\天龙八部-网络版.txt", "r", encoding='utf-8')
fo = open("E:\\bd\\caozuo\\stu\\do\\2\\天龙八部-汉字统计.txt", "w", encoding='utf-8')
txt = fi.read()
d = {}
for c in txt:
    d[c] = d.get(c, 0) + 1
del d[' ']
del d['\n']
ls = []
for key in d:
    ls.append("{}:{}".format(key, d[key]))
fo.write(",".join(ls))
fi.close()
fo.close()

"""
"""

import jieba
fi = open("E:\\bd\\caozuo\\stu\\do\\2\\天龙八部-网络版.txt", "r", encoding='utf-8')
fo = open("E:\\bd\\caozuo\\stu\\do\\2\\天龙八部-词语统计.txt", "w", encoding='utf-8')
t = fi.read()

txt = jieba.lcut(t)
d = {}
for c in txt:
    d[c] = d.get(c, 0) + 1
del d[' ']
del d['\n']
ls = []
for key in d:
    ls.append("{}:{}".format(key, d[key]))
fo.write(",".join(ls))
fi.close()
fo.close()
"""


     
