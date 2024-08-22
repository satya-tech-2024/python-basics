names = ['Satya', 'Subha','Siddharth','Shourya']

print(names[-2])
print(names[0:-1])

names[0] = 'SatyaJ'

print(names)

names.append("Josyula")
print(names)
names.pop()
print(names)
names.insert(2, "People")
print(names)
names.remove("People")
print(names)
# names.clear()
# print(names)
names.sort()
print(names)
names.reverse()
print(names)
n2 = names.copy()
n2.append("All")
print(n2)