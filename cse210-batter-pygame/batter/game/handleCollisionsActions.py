from game.actor import Actor
from game import constants
from game.point import Point
from game.audio_service import AudioService

class HandleCollisionsActions(Actor):
    def __init__(self, physics_service, score):
        super().__init__()

        self.physics = physics_service
        self.audio = AudioService()
        self._score = score

    def execute(self, cast):
        ball = cast["balls"][0]
        paddle = cast["paddle"][0]
        bricks = cast["bricks"]

        self.paddle_collision(ball, paddle)
        self.brick_collision(ball, bricks)

    def paddle_collision(self, ball, paddle):
        if self.physics.is_collision(ball, paddle):
            dx = ball.get_velocity().get_x()
            dy = ball.get_velocity().get_y()

            point = Point(dx, dy * -1)
            ball.set_velocity(point)

    def brick_collision(self, ball, bricks):
        collision_count = 0
        destroy = -1
        for count in range(len(bricks)):
            if self.physics.is_collision(ball, bricks[count]):
                dx = ball.get_velocity().get_x()
                dy = ball.get_velocity().get_y()

                collision_count += 1
                self.audio.play_sound(constants.SOUND_BOUNCE)

                if collision_count < 2:
                    point = Point(dx, dy * -1)
                    ball.set_velocity(point)

                destroy = count
        if destroy >= 0:
            bricks.pop(destroy)
            self._score.count_points(5)
            

