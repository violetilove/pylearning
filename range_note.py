numbers_1_s = range(1, 5)        # number_1_s这里并不是列表，而是迭代器
print(numbers_1_s)
for numbers_1 in numbers_1_s:    # 打印出1~4，range()让Python从指定的第一个值开始数，并在到达你指定的第二个值时停止，
    print(numbers_1)             # 因为它在第二个值处停止，所以输出不包含该值
print("\n")
for number in range(5):          # range(5)返回0~4
    print(number)
print("\n")
number_2_s = list(range(2, 11, 2))   # list()可以将range()的输出转换为列表
print(number_2_s)                    # range()的第三个参数可以指定步长
print("\n")
number_3_s = [1.0, 2.0, 3.0, 4.0, 5.0]
print(f"Max={max(number_3_s)}, Min={min(number_3_s)}, Sum={sum(number_3_s)}")  # max(）、min()、sum()可用于整数和浮点数
print("\n")
number_4_s = [value**2 for value in range(1, 11)]         # 列表解析
print(number_4_s)
