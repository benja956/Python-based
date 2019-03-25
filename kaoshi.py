fi = open("E:\\bd\\caozuo\\stu\\do\\1\\论语-网络版.txt", "r", encoding="utf-8")
fo = open("E:\\bd\\caozuo\\stu\\do\\1\\论语-提取版.txt", "w")
wflag = False            #写标记
for line in fi:
    if "【" in line:     #遇到【时，说明已经到了新的区域，写标记置否
        wflag = False
    if "【原文】" in line:  #遇到【原文】时，设置写标记为True
        wflag = True
        continue    
    if wflag == True:    #根据写标记将当前行内容写入新的文件
        for i in range(0,10):
            for j in range(0,10):
                line = line.replace("{}·{}".format(i,j),"**")
        for i in range(0,10):
            line = line.replace("*{}".format(i),"")
        for i in range(0,10):
            line = line.replace("{}*".format(i),"")
        line = line.replace("*","") 
        fo.write(line)
fi.close()
fo.close()
