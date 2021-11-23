from game.actor import Actor
from game import constants
from game.point import Point

class Paddle(Actor):
    def __init__(self):
        super().__init__()

        self.set_image(constants.IMAGE_PADDLE)
        self.set_width(constants.PADDLE_WIDTH)
        self.set_height(constants.PADDLE_HEIGHT)

        x = constants.PADDLE_X
        y = constants.PADDLE_Y
        position = Point(x,y)
        self.set_position(position)
