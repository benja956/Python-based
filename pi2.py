import random
a = 0
b = 19999999
for i in range(b):
     x = random.random()
     y = random.random()
     z = pow((x*x+y*y),0.5)
     if z < 1:
          a += 1
     else:
          a += 0
pi = (4 * a / b)
     
     

print("{}".format(pi))
