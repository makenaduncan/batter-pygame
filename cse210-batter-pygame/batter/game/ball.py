from game.actor import Actor
from game import constants
from game.point import Point

class Ball(Actor):
    def __init__(self):
        super().__init__()
        self.set_image(constants.IMAGE_BALL)
        self.set_width(constants.BALL_WIDTH)
        self.set_height(constants.BALL_HEIGHT)

        x = constants.BALL_X
        y = constants.BALL_Y
        position = Point(x,y)

        self.set_position(position)

        dx = constants.BALL_DX
        dy = constants.BALL_DY
        velocity = Point(dx,dy)

        self.set_velocity(velocity)