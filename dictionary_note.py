human_0 = {'gender': 'man', 'age': 26}          # 创建字典
# human_0 = {} 或者创建一个空字典，再依次添加
print(f"{human_0['gender']} {human_0['age']}")
print(human_0)
human_0['weight'] = '56kg'                        # 添加键值对，元素的排列顺序与添加顺序一致
human_0['height'] = '170cm'
print(human_0)
human_0['age'] = 27         # 修改键值对
print(human_0)
del human_0['age']          # 删除键值对，删除的键会永久消失
print(human_0)
favorite_languages = {                   # 由类似对象组成的字典
    'jen': 'python',                     # 在最后一个键值对后面也加上逗号，为添加下一个键值对做好准备
    'sarah': 'c',
    'phil': 'ruby',
}
# get()的第一个参数用于指定键，第二个参数为指定的键不存在时要返回的值，是可选的
favorite_language = favorite_languages.get('jen', 'No existing')
print(favorite_language)
favorite_language = favorite_languages.get('shy', 'No existing')
print(favorite_language)
favorite_language = favorite_languages.get('shy')   # 调用get()时，如果没有指定第二个参数且指定的键不存在，Python将返回值None，
print(favorite_language)                            # 这个特殊值表示没有相应的值，而是一个表示所需值不存在的特殊值
