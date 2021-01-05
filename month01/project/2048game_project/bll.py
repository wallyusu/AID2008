from model import GameModel
import random

class GameController:
    def __init__(self):
        self.view = GameModel()
        self.list_merge = [2, 0, 2, 0]
        self.map = [
            [2, 0, 0, 2],
            [4, 2, 0, 2],
            [2, 4, 2, 4],
            [0, 4, 0, 4],
]

    def zero_to_end(self):
        """
            零元素向后移动
            思想：从后向前判断，如果是0则删除,在末尾追加.
        """
        for i in range(len(self.list_merge) - 1, -1, -1):
            if self.list_merge[i] == 0:
                del self.list_merge[i]
                self.list_merge.append(random.choice([0,2]))

    def merge(self):
        """
            合并
              核心思想：零元素后移，判断是否相邻相同。如果是则合并.
        """
        self.zero_to_end()
        # [4,4,4,4]
        for i in range(len(self.list_merge) - 1):  # 取前三个  i
            if self.list_merge[i] == self.list_merge[i + 1]:  # 与下一个比 i + 1
                self.list_merge[i] += self.list_merge[i + 1]
                del self.list_merge[i + 1]  # 删除下一个(因为不是当前,所以不存在漏删)
                self.list_merge.append(random.choice([0,2]))  # 因为删除一个,补充一个,所以不存在越界
                # self.random_num() # 每次合并后,随机改变一个为0的数字为2


    def move_left(self):
        """
            向左移动map
            思想：获取每行，交给list_merge，在通知merge()进行合并
        :return:
        """
        # global self.list_merge
        for line in self.map:
            self.list_merge = line
            self.merge()

    def move_right(self):
        """
            向左移动map
            思想：获取每行，交给list_merge，在通知merge()进行合并
        :return:
        """
        # global list_merge
        for line in self.map:
            # 从右向左获取数据形成新列表
            self.list_merge = line[::-1]
            # 处理数据
            self.merge()
            # 将处理后的数据再从右向左还给map
            line[::-1] = self.list_merge

    def transport(self):
        # global list_merge
        for i in range(1, len(self.map)):
            for j in range(i, len(self.map)):
                self.map[j][i - 1], self.map[i - 1][j] = self.map[i - 1][j], self.map[j][i - 1]

    def move_up(self):
        self.transport()
        self.move_left()
        self.merge()
        self.transport()

    def move_down(self):
        self.transport()
        self.move_right()
        self.merge()
        self.transport()

    # def random_num(self):
    #     if self.list_merge[3] == 0:
    #         del self.list_merge[3]
    #         self.list_merge.append(random.choice([0,2]))


    def game_over(self):
        for item in self.list_merge:
            if item == 2048:
                print('恭喜你，赢了！')
            break
        # if self.list_merge[0] != 0 and self.list_merge[1] != 0 and self.list_merge[2] != 0 and self.list_merge[3] != 0:
        #     print('游戏结束,你输了！')

