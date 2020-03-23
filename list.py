# numbers = [1, 2, 3, 4]
# squares = []
# for n in numbers:
#     squares.append(n**2)
# print(squares)

# list_a = [1, 2, 3, 4]
# list_b = [2, 3, 4, 5]
# common_num = []
# for a in list_a:
#     for b in list_b:
#         if a == b:
#             common_num.append(a)

# print(common_num)


# list_a = [1, 2, 3, 4]
# list_b = [2, 3, 4, 5]
# common_num = [a for a in list_a for b in list_b if a == b]
# print(common_num)

# list_a = ["Hello", "Wolrld", "in", "Python"]
# small_list_a = [_.lower() for _ in list_a]
# print(small_list_a)

list_a = range(1, 10, 2)
x = [[a**2, a**3] for a in list_a]
print(x)