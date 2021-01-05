# x,y = (20,30)
# print(x,y)
# x,y = 20,30
# print(x,y)

# l=[1,2,3]
# print(l.__dict__)
# print(l.__class__)
# print(l.__doc__)

# a = [1]
# b = [1,2]
# print(a )

list01 = [43,43,54,56,76,87,98]
def find_none():
    for i in range(len(list01)):
        if list01[i] % 2 != 0:
            list01[i] = None

find_none()
print(list01)
