ls = [1,4,3,3,2,2,3,"q","w","e","r"]
ls.append("x")

ls.insert(0,5)
del ls[::3]
print(ls)

lt = []

lt += [1,2,3,4,5]

lt[2] = 6

lt.insert(2,"x")

del lt[1]

del lt[1:4]

0 in lt

lt.append(0)

lt.index(0)

len(lt)

max(lt)

lt.clear()

print(lt)
