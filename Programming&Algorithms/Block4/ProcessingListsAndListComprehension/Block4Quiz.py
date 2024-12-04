var1 = [9, 8, 7, 6, 5]

var1.insert(3, 4)

print(var1)

var1 = [10, 20, 30, 40]

var1.append(55)

print(var1)



list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [list1[i] for i in range(3, 7)]
print(list2)


list1 = [2, 22, 41, 80, 3, 7, 98, 10, 5]

my_list = [n for n in list1 if n > 5 and n < 50]

print(my_list)


m = 6
for e in range(0, 9, 3):
    m /= 2
print(m)

q = 7
if(q >= 2):
    q += 7
print(q)

c = 0
for k in range(0, 9, 2):
  for x in range(0, -5, -2):
    c += 1
print(c)