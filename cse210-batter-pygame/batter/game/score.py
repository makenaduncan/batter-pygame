from game.actor import Actor
from game import constants
from game.point import Point

class Score(Actor):
    def __init__(self):
        super().__init__()
        self._score = 0
        self._score_display()


    def _score_display(self):
        self.set_position(Point((constants.MAX_X / 8) - constants.SCORE_WIDTH, constants.MAX_Y / 2))
        self.set_width(constants.SCORE_WIDTH)
        self.set_text(f"Your Score: {self._score}")

    def count_points(self, points):
        self._score += points
        self.set_text(f"Your Score: {self._score}")