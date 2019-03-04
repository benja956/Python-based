#weekname.py
weekStr = "星期一星期二星期三星期四星期五星期六星期日"
x = eval(input("请输入你想知道的星期："))
y = (x - 1) * 3
print(weekStr[y:y+3])

weekStr2 = "一二三四五六日"
a = eval(input("请输入你想知道的星期："))
print("星期" + weekStr2[a-1])
