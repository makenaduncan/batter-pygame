import sys
from game.point import Point
import pygame

class InputService:
    """Detects player input. The responsibility of the class of objects is to detect player keypresses and translate them into a point representing a direction (or velocity).

    Stereotype: 
        Service Provider

    Attributes:
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (InputService): An instance of InputService.
        """
        if not pygame.get_init():
            pygame.init()

    def get_direction(self):
        """Gets the selected direction based on the currently pressed keys.

        Args:
            self (InputService): An instance of InputService.

        Returns:
            Point: The selected direction.
        """
        dx = 0
        dy = 0

        if self.is_left_pressed():
            dx = -1
        
        if self.is_right_pressed():
            dx = 1
        
        if self.is_up_pressed():
            dy = -1
        
        if self.is_down_pressed():
            dy = 1

        direction = Point(dx, dy)
        return direction

    def is_left_pressed(self):
        return self.is_key_pressed(pygame.K_LEFT)

    def is_right_pressed(self):
        return self.is_key_pressed(pygame.K_RIGHT)

    def is_up_pressed(self):
        return self.is_key_pressed(pygame.K_UP)

    def is_down_pressed(self):
        return self.is_key_pressed(pygame.K_DOWN)

    def get_keys_state(self, *keys):
        """
            keys: a tuple of keys that whoever calls this function
                wants to check whether is pressed.
                Each key is represented by an integer stored in genie.constants.keys
            
            Return Value:
                The function will return a DICT that maps the key to either 1 or 0,
                    with 1 meaning the key is pressed and 0 meaning it's not pressed.
            
            Note: There is a chance that some keys might not get detected if multiple
                keys are pressed at the same time
        """
        pygame.event.pump()
        keys_pressed = {}
        keys_state = pygame.key.get_pressed()
        for key in keys:
            keys_pressed[key] = keys_state[key]
        
        return keys_pressed

    def is_key_pressed(self, key):
        """
            check to see if a key is pressed. Returns True for pressed and False for released
        """
        keys_state_dict = self.get_keys_state(key)
        return keys_state_dict[key]
    
    def is_key_released(self, key):
        """
            Similar to is_key_pressed, but returns True for released and False for pressed
        """
        keys_state_dict = self.get_keys_state(key)
        return keys_state_dict[key] ^ 1