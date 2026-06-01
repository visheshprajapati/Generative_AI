a={1,2,3,4,5}
b={3,4,5,6,7}

a.add(7)
print(a)

a.update(b)
print(a)

a.remove(3)
print(a)

a.discard(7)
print(a)

a.pop()
print(a)

#a.clear()
#print(a)

c=a.union()
print(c)

z=a.intersection()
print(z)

d=a.difference(b)
print(d)

s=a.symmetric_difference(b)
print(s)

i=a.issubset(b)
print(i)

sup=a.issuperset(b)
print(a)

