"""
 将列表中的数字累减
    list02 = [5, 1, 4, 6, 7, 4, 6, 8, 5]
    提示：初始为第一个元素
"""
# list02 = [5, 1, 4, 6, 7, 4, 6, 8, 5]
# list_sum = 5
# for number in range(1,len(list02)):
#     list_sum -= list02[number]
# print(list_sum)

"""
将列表中整数的十位不是3和7和8的数字存入另外一个列表
   list03 = [135, 63, 227, 675, 470, 733, 3127]
   结果:[63, 227, 3127]
   提示：将数字转换为字符串进行处理
"""

# list03 = [135, 63, 227, 675, 470, 733, 3127]
# list02 =[str(number) for number in list03]
# list_sum = []
# for message in list02:
#     if message[-2] not in ('3','7','8'):
#         list_sum.append(int(message))
# print(list_sum)


"""
在数字列表中查找最大的数字(不许用内置函数)
    算法：
        [170  ,  160  ,  180  ,  165]
    假设第一个就是最大值
    使用假设的和第二个进行比较, 发现更大的就替换假设的
    使用假设的和第三个进行比较, 发现更大的就替换假设的
    使用假设的和第四个进行比较, 发现更大的就替换假设的
    最后，假设的就是最大的.
"""
# list_number = [170,160,180,165]
# list_max = 0
# for item in range(len(list_number)):
#     if list_number[item-1] < list_number[item]:
#         list_max = list_number[item]
#     else:
#         list_max = list_number[item-1]
# print(list_max)

"""
列表推导式练习：
  计算1970年到2050年之间所有闰年
"""


# for year in range(1970,2051):
#     if year % 4 == 0 and year % 400 != 0 or year % 400 == 0:
#         print(year,end=' ')

"""

将列表中所有元素转换为一个字符串
    列表:["我", "爱", "你", "p", "y", "t", "h", "o", "n", 666]
    结果:我爱你python666
  注意：列表中包含非字符串数据
"""
# list_love = ["我", "爱", "你", "p", "y", "t", "h", "o", "n", 666]
# # list_love01 = [str(i) for i in list_love]
# # result = ''.join(list_love01)
# # print(result)

"""
在终端中获取颜色(RGBA),打印描述信息,否则提示颜色不存在
    "R" -> "红色"
    "G" -> "绿色"
    "B" -> "蓝色"
    "A" -> "透明度"
   提示：使用字典存储数据
"""
dict_color = {"R":"红色","G":"绿色","B":"蓝色","A":"透明度"}
color_write = input("请获取颜色： ")
# if color_write not in dict_color:
#     print("颜色不存在")
# else:
#     print(dict_color[color_write])