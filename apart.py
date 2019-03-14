import numpy,csv
"""
fo = open("D:\\Python-based\\apart.csv")
ls = []
for line in fo:
     line = line.replace("\n","")
     ls.append(line.split(","))
fo.close     
f1 = open("D:\\Python-based\\add.csv")
add = []
for line in f1:
     line = line.replace("\n","")
     add.append(line.split(","))
f1.close

print(ls,add)
"""

with open('D:\\Python-based\\apart.csv','r') as csv_f:
    reader = csv.reader(csv_f)
    fieldnames = next(reader)
    csv_reader = csv.DictReader(csv_f,fieldnames=fieldnames)
    for row in csv_reader:
        d = {}
        for k, v in row.items():
            d[k] = v
        print(d)
with open('D:\\Python-based\\add.csv','r') as csv_add:
    addreader = csv.reader(csv_add)
    addnames = next(addreader)
    csvadd_reader = csv.DictReader(csv_add,fieldnames=addnames)
    for row in csvadd_reader:
        add = {}
        for f, s in row.items():
            add[f] = s
        print(add)
