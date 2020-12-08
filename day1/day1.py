import itertools


f = open("input.txt", "r")



list = []
for i in f:
    list.append(int(i))

print(len(list))
combitations = itertools.combinations(list, 3)
for i in combitations:
     if i[0] + i[1] + i[2] == 2020:
         print(i[0] * i[1] * i[2])
         
