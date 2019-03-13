import pkuseg
txt = open("gov.txt","r").read()
seg = pkuseg.pkuseg()
counts = {}
govtxt = seg.cut(txt)

excludes = {}

for word in govtxt:
     if len(word) == 1:
          continue
     else:
          counts[word] = counts.get(word,0)+1
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(50):
     word,count = items[i]
     print("{0:<10}{1:>5}".format(word,count))
