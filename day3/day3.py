#  Part 1

lines = open("input3.txt", "r")
lines_list = list(map(lambda s: s.strip(), lines))

INPUT_WIDTH = len(lines_list[0])


index = 2
trees = 0
number = 2

for line in lines_list[2:]:
    if number % 2 == 0:
        if line[index-1] == "#":
            trees += 1
        index += 1
        if index > INPUT_WIDTH:
            index = index - INPUT_WIDTH
    number += 1

print(trees)


# right 1: 84
# right 3: 198
# right 5: 72
# right 7: 81
# right 1, down 2: 53
