dimensions = (200, 50)
print(dimensions[0], dimensions[1])
# dimension[0] = 250 该语句不可行，试图修改元组的操作是不被允许的
my_t = (3,)
# 严格地说，元组是由逗号标识的，圆括号只是让元组看起来更整洁、更清晰，
# 如果你要定义只包含一个元素的元组，必须在这个元素后面加上括号，
# 创建只包含一个元素的元组通常没有意义，但自动生成的元组有可能只有一个元素
dimensions = (400, 50)
# 将一个新元组关联到变量dimensions，虽然不能修改元组的元素，但可以给存储元组的变量赋值
