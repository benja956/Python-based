'''
a,b,c =eval(input())
p = (a+b+c)/2
area = (p*(p-a)*(p-b)*(p-c))**0.5
print("{:.2f}".format(area))

ls = eval(input())
for i in range(len(ls)):
    ls[i] = ls[i].capitalize()

print(ls)

def mean(numlist):
    s = 0.0
    for num in numlist:
        s = s + num
    return s/len(numlist)
def dev(numlist,mean):
    sdev = 0.0
    for num in numlist:
        sdev = sdev + (num - mean)**2
    return (sdev /(len(numlist)-1) )** 0.5
#请输入一个列表：
ls = eval(input(""))
print("均方差为：{:.2f}".format(dev(ls,mean(ls))))

# 从csv文件中读取考勤数据
ls = []
for i in range(1,11):
    fo =  open(str(i) +".csv","r",encoding = "utf-8")
    for line in fo:
        line = line.replace("\n","")
        ls.append(line.split(",")[0])        
    fo.close()
counts = {}
for name in ls:
    counts[name] = counts.get(name,0) + 1
items = list(counts.items())
print("全勤同学有：",end ="")
for i in range(1,74,1):
    word,count = items[i]
    if count == 10 :
        #print("{0:<10}:{1:<5}次".format(word,count))
        print(word,end =",")

    '''


fo = open("sgldout.txt","r",encoding ="utf-8")
words = fo.readlines()
fo.close()

sym = "；。，“”： "
DictWords = {}
for ls in words:
    if ls[:-1] not in sym:
        DictWords[ls[:-1]] = DictWords.get(ls[:-1], 0) + 1
        L = list(DictWords.items())
        L.sort(key = lambda s:s[1],reverse=True)
# 输出到文件
fo = open("sgldstatistics.txt", "w", encoding="utf-8")
for i in range(5):
    fo.write(L[i][0] + ":" + str(L[i][1]) + "\n")
fo.close()
# print 输出
for i in range(5):
    print(L[i][0] + ":" + str(L[i][1]))
