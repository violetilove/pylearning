numbers = list(range(6))
print(numbers)               # 原列表
print(numbers[0:3])          # 返回索引为0、1、2的元素
print(numbers[1:4])          # 返回索引为1、2、3的元素
print(numbers[:4])           # 没有指定第一个索引，Python将自动从列表开头开始
print(numbers[2:])           # 切片中止于列表末尾，返回从索引为2的元素到列表末尾的所有元素
print(f"{numbers[-3:]} {numbers[:-3]}")          # 输出列表中的最后三个元素、输出从列表开头到倒数第三个元素的所有元素
print(numbers[:])            # 表示提取整个列表
print(numbers[::2])          # 在切片的方括号内指定第三个值，表示在指定范围内每隔多少元素提取一个
print("\n")

numbers_2 = numbers[:]       # 复制列表需要创建一个包含整个列表的切片，即整个列表的副本
numbers.append(6)
numbers_2.append(7)
print(numbers)
print(numbers_2)             # 通过打印结果可知numbers和numbers_2分别为两个列表
print("\n")

numbers_3 = list(range(6))
numbers_4 = numbers_3        # 实际上Python将新变量numbers_4关联到已与number_3想关联的列表，因此这两个变量指向同一列表
numbers_3.append(6)
numbers_4.append(7)
print(numbers_3)
print(numbers_4)             # 打印结果相同
print("\n")

origin_number = 3
next_number = origin_number
print(f"origin_number is {origin_number}, next_number is {next_number}")
origin_number = 4
print(f"origin_number is {origin_number}, next_number is {next_number}")      # 单独的字符串或则数可以直接赋值
