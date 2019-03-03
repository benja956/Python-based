#santiandayu.py
dayup = 1
for i in range(365):
    if i % 5 in [4,5]:
       dayup = dayup * 0.99
    else:
         dayup = dayup * 1.01
print("三天打鱼两天晒网只有：{:.3f}".format(dayup))

ddup = 1
for i in range(365):
    if i % 7 in [6,0] :
        ddup = ddup * 0.99
    else:
        ddup = ddup * 1.02
print("多一份努力的收获是：{:.3f}".format(ddup))	   

dup = 1
for i in range(365):
    if i % 7 in [6,0] :
        dup = dup * 1.01
    else:
        dup = dup * 0.99
print("多一份懈怠的收获是：{:.3f}".format(dup))	
