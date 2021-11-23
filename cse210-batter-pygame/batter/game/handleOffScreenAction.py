from game import constants
from game.action import Action
from game.point import Point



class HandleOffScreenAction(Action):
    def execute(self, cast):
        ball = cast["balls"][0]
        paddle = cast["paddle"][0]
        self.is_ball_off(ball)
        self.is_paddle_off(paddle)


    def is_ball_off(self, ball):
        x = ball.get_position().get_x()
        y = ball.get_position().get_y()
        dx = ball.get_velocity().get_x()
        dy = ball.get_velocity().get_y()

        if x <= 0 or (x + ball.get_width()) >= (constants.MAX_X):
            dx *= -1
        if y <= 5: 
            dy *= -1
        if y >= constants.MAX_Y -5:
            self.cast["balls"].pop

        point = Point(dx, dy)
        ball.set_velocity(point)

    def is_paddle_off(self, paddle):
        x = paddle.get_position().get_x()
        y = paddle.get_position().get_y()
        dx = paddle.get_velocity().get_x()
        dy = paddle.get_velocity().get_y()

        if (x <= 5 and dx < 0) or ((x + paddle.get_width()) >= constants.MAX_X and dx > 0):
            dx = 0
        if (y <= 5 and dy < 0) or ((y + paddle.get_height()) >= constants.MAX_Y -1 and dy > 0):
            dy = 0

        point = Point(dx, dy)
        paddle.set_velocity(point) 