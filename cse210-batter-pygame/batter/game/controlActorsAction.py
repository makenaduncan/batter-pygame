from game import constants
from game.action import Action

class ControlActorsAction(Action):
    def __init__(self, input_service):
        self.__input_service = input_service

    def execute(self, cast):
        direction = self.__input_service.get_direction()
        paddle = cast["paddle"][0]
        paddle.set_velocity(direction.scale(constants.PADDLE_SPEED))
