import time
# tuple_time = time.localtime()
# print(tuple_time)
# print(tuple_time[-6:-3])
# print(tuple_time[3:6])

# print(time.localtime(1600413415.692054))
# print(time.mktime(tuple_time))
# print(time.strptime("2020/09/18 15:30:38","%Y/%m/%d %H:%M:%S"))

# def get_week(year,month,day):
#     tuple_time = time.strptime(f'{year}/{month}/{day}','%Y/%m/%d')
#     index_week = tuple_time[6]
#     tuple_week = ('星期一','星期二','星期三','星期四','星期五','星期六','星期日')
#     print(tuple_week[index_week])

# get_week(2020,9,18)

# def get_birthday(year,month,day):
#     tuple_time = time.strptime(f"{year}/{month}/{day}", "%Y/%m/%d")
#     all_mktime = time.time() - time.mktime(tuple_time)
#     day01 = all_mktime / 3600 / 24
#     print(f'活了{day01:.0f}天')
#
# get_birthday(1987,1,30)

# print(time.time())
# def get_score():
#     try:
#         score = int(input('输入成绩：　'))
#         return score
#     except ValueError:
#         print('成绩录入失败')
#
# score = get_score()
# print(f'成绩是：{score}')

