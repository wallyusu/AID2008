class A:
    a = 2
    def __init__(self):
        self.v = 100


class B(A):
    a = 3
    def __init__(self):
        self.v = 200
        super().__init__()
a1 = B()
print(a1.a)