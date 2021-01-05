from bll import GameController
class GameView:
    def __init__(self):
        self.controller = GameController()


    def set_type(self):
        for num in self.controller.map:
            print(num)

    def main(self):
        while True:
            self.set_type()
            self.controller.game_over()
            direction = input('--------我是分割线--------')
            if direction == 'w':
                self.controller.move_up()
            elif direction == 's':
                self.controller.move_down()
            elif direction == 'a':
                self.controller.move_left()
            elif direction == 'd':
                self.controller.move_right()
