
class Teacher:
    def __init__(self,name,age,address=''):
        self.address = address

    def infos(self):
        print(self.name,self.age,self.address)

t1 = Teacher()
t1.infos()