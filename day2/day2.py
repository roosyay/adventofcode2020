lines = open("input2.txt", "r")
lines_list = list(map(lambda s: s.strip(), lines))


# #  part 1
# result = 0
# for i in lines_list:
#     index = i.index(':')
#     letter = (i[index-1])
#     password = (i[index+2:])
#     dash = i.index('-')
#     min = int(i[:dash])
#     max = int(i[dash+1:i.find(' ')+1])
#     occurrences = (password.count(letter))
#
#     if occurrences in range(min, max+1):
#         result += 1
#
# print(result)

#  part 2
result = 0
for i in lines_list:
    index = i.index(':')
    letter = (i[index-1])
    password = (i[index+2:])


    dash = i.index('-')
    min = int(i[:dash])
    max = int(i[dash+1:i.find(' ')+1])

    index1 = password[min-1]
    index2 = password[max-1]

    if  index1 == letter and index2 == letter:
        continue
    elif index1 == letter or index2 == letter:
        result += 1

print(result)
