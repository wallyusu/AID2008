"""
(1). 根据格式打印老婆对象:xx的身高是xx,颜值是xx.
    效果：print(Wife("双儿", 170, 98))
         双儿的身高是170,颜值是98.
"""


class Wife:
    def __init__(self, name='', height=0, face_score=0):
        self.name = name
        self.height = height
        self.face_score = face_score

    def __str__(self):
        return f'{self.name}的身高是{self.height},颜值是{self.face_score}'


# 调用
# sr = Wife("双儿", 170, 98)
# print(sr)

"""
(2). 判断阿珂是否在列表中
"""
class Wife:
    def __init__(self, name='', height=0, face_score=0):
        self.name = name
        self.height = height
        self.face_score = face_score

    # 比较是否相同的判断标准
    def __eq__(self, other):
        return self.name == other.name
    # 比较是否大小的判断标准，从小到大排序
    def __lt__(self, other):
        return self.face_score < other.face_score

    def __str__(self) -> str:
        return f'{self.name}的身高是{self.height},颜值是{self.face_score}'


list_wife = [
    Wife("双儿", 170, 98),
    Wife("阿珂", 173, 100),
    Wife("苏荃", 160, 99),
    Wife("丽丽", 167, 90),
    Wife("芳芳", 168, 92),
    Wife("苏荃", 160, 99),

]
# 调用
# ake = Wife("阿珂", 173, 100)
# print(ake in list_wife)

"""
(3). 计算苏荃在列表中存在的个数
"""
# sq = Wife("苏荃", 160, 99)
# print(list_wife.count(sq))
# print(list_wife.index(sq)) # 查找苏荃在列表中的索引位置


"""
(4). 查找颜值最高的老婆对象
"""
# max_face = max(list_wife)
# print(max_face)

"""
(5). 根据颜值对老婆列表进行升序排列
"""
# list_wife.sort()
# print(list_wife)

"""
4. 小明使用手机打电话
   要求:增加座机,卫星电话时不影响小明.
"""
class Person:
    def __init__(self,name):
        self.name = name

    def use(self,phone):
        print(self.name,'使用',phone.name)
        phone.to_call()

class Phone:
    def __init__(self,name):
        self.name = name

    def to_call(self):
        print('打电话,滴滴滴...')

class Landline_phone(Phone):
    def to_call(self):
        super().__init__(name='')
        print('打电话,嘟嘟嘟...')

class Satellite_phone(Phone):
    def to_call(self):
        super().__init__(name='')
        print('打电话,咻咻咻...')
# 调用
# xm = Person('小明')
# sj = Phone('手机')
# zj = Landline_phone('座机')
# wx = Satellite_phone('卫星')
# xm.use(wx)

"""
5. 画出下列代码内存图
map = [
    [2, 2, 8, 16],
    [4, 2, 0, 2],
    [2, 4, 2, 4],
    [0, 4, 0, 4],
]
list_merge = map[0]
list_merge[0] = 0 # 通过list_merge修改数据,等同于修改
print(map[0][0])# 0

list_merge = map[1][::-1] # 创建新容器[2,0,2,4]
list_merge[0] = 0 # [0,0,2,4]
map[1][::-1] = list_merge
print(map[1]) # [4,2,0,0]
"""
