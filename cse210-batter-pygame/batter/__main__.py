import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.draw_actors_action import DrawActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService
from game.audio_service import AudioService
from game.brick import Brick
from game.ball import Ball
from game.paddle import Paddle
from game.controlActorsAction import ControlActorsAction
from game.handleCollisionsActions import HandleCollisionsActions
from game.handleOffScreenAction import HandleOffScreenAction
from game.moveActorsAction import MoveActorsAction
from game.score import Score

def main():

    # create the cast {key: tag, value: list}
    cast = {}

    score = Score()

    cast["bricks"] = []
    bricks = []
    for i in range (15):
        for n in range(8):
            brick = Brick()
            position = Point(25+(i*50), 20+(n*30))
            brick.set_position(position)
            bricks.append(brick)
    cast["bricks"] = bricks
    # TODO: Create bricks here and add them to the list

    cast["balls"] = []
    balls = []
    ball = Ball()
    balls.append(ball)
    cast["balls"] = balls

    # TODO: Create a ball here and add it to the list

    cast["paddle"] = []
    paddles = []
    paddle = Paddle()
    paddles.append(paddle) 
    cast["paddle"] = paddles
    # TODO: Create a paddle here and add it to the list

    cast["score"] = [score]

    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()

    draw_actors_action = DrawActorsAction(output_service)
    moveActorsAction = MoveActorsAction()
    handleOffScreenAction = HandleOffScreenAction()
    controlActorsAction = ControlActorsAction(input_service)
    handleCollisionsActions = HandleCollisionsActions(physics_service, score)

    # TODO: Create additional actions here and add them to the script

    script["input"] = [controlActorsAction]
    script["update"] = [handleOffScreenAction, handleCollisionsActions, moveActorsAction]
    script["output"] = [draw_actors_action]



    # Start the game
    output_service.open_window("Batter")
    audio_service.start_audio()
    audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio()

if __name__ == "__main__":
    main()