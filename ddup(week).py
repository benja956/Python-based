x = 1

for i in range(52):
    for o in range(2):
       x = x * 0.99
    for p in range(5):
       x = x * 1.01
print("{:.2f}".format(x))
