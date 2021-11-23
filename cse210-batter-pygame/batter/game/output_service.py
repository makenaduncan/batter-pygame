import sys
from game import constants
import pygame

class OutputService:
    """Outputs the game state. The responsibility of the class of objects is to draw the game state on the terminal. 
    
    Stereotype: 
        Service Provider

    Attributes:
        None
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (OutputService): An instance of OutputService.
        """
        if not pygame.get_init():
            pygame.init()
        self._images_cache = {}
        self._window = None
        self._font = pygame.font.SysFont(None, 24)
        self._clock = pygame.time.Clock()

    def open_window(self, title):
        """
        Opens a new window with the provided title.
        """
        self._window = pygame.display.set_mode((constants.MAX_X, constants.MAX_Y))
        pygame.display.set_caption(title)

    def draw_image(self, x, y, image_path):
        
        # put image in cache so we don't have to load again
        if (image_path not in self._images_cache.keys()):
            image = pygame.image.load(image_path)
            self._images_cache[image_path] = image

        image = self._images_cache[image_path]

        self._window.blit(image, (x, y))


    def clear_screen(self):
        self._clock.tick(30)
        self._window.fill(constants.BACKGROUND_COLOR);

    def draw_box(self, x, y, width, height, color=(100, 100, 255)):
        """
        Draws at rectangular box with the provided specifications.
        """
        self._draw_rectangle((x, y), width, height, color=color)

    def _draw_rectangle(self, center, width : int, height: int, color : tuple = (0, 0, 0), 
                        border_width : int = 0, border_radius : int = 0, border_top_left_radius : int = -1,
                        border_top_right_radius : int = -1, border_bottom_left_radius : int = -1, 
                        border_bottom_right_radius : int = -1):
        """
            Draw a rectangle.

            Input:
                - center: An (x, y) tuple indicating the center of the rectangle
                - width: the width of the rectangle
                - height: the height of the rectangle
                - color: An RGB tuple. (0,0,0) is BLACK, and (255,255,255) is WHITE
                        You can also pass a 4 entries tuple. the 4th entry determines opacity
                - border_width: how many pixels you want the border to be
                
                - border_radius, border_..._radius: use these parameters if you want your rectangle
                                     to have rounded corners.
                                        + values < 1 means squared corners
                                        + values >= 1 means rounded corners. Increase this
                                            to increase the roundness
        """
        pygame.draw.rect(self._window, color, pygame.Rect(center[0] - width / 2, center[1] - height / 2, width, height),
                        border_width, border_radius, border_top_left_radius, border_top_right_radius, border_bottom_left_radius,
                        border_bottom_right_radius)
   


    def draw_text(self, x, y, text, is_dark_text):
        color = constants.COLOR_BLACK if is_dark_text else constants.COLOR_WHITE

        self._draw_text(text, position=(x, y), color=color)

    def _draw_text(self, text : str, font : str = None, font_size : int = 24, 
                    color : tuple = (0, 0, 0), position : tuple = (0, 0),
                    antialias : bool = True, position_center : bool = False):
        """
            Draw the input text (str).
            Inputs:
                - text: The text you want to draw
                - font: The font you want to use (try to find out what's
                        available on your system first)
                - font_size: default is 24
                - color: An RGB tuple. (0,0,0) is BLACK, and (255,255,255) is WHITE
                        You can also pass a 4 entries tuple. the 4th entry determines opacity
                - position: A tuple in the form of (x, y)
                - antialias: Boolean. Default is True
                - position_center: A boolean that tells whether the position given should be
                                    the center of the text image or the top-left corner.
                        + True: treats the position as the center of the text image
                        + False: treats the position as the top-left corner of the text image

        """
        text_image = self._font.render(text, antialias, color)
        txt_img_position = position

        self._window.blit(text_image, txt_img_position)

    def draw_actor(self, actor):
        """Renders the given actor's text on the screen.

        Args:
            self (OutputService): An instance of OutputService.
            actor (Actor): The actor to render.
        """ 
        position = actor.get_position()
        x = position.get_x()
        y = position.get_y()
        width = actor.get_width()
        height = actor.get_height()

        if actor.has_image():
            image = actor.get_image()
            self.draw_image(x, y, image)
        elif actor.has_text():
            text = actor.get_text()
            self.draw_text(x, y, text, False)
        elif width > 0 and height > 0:
            self.draw_box(x, y, width, height)
        
    def draw_actors(self, actors):
        """Renders the given list of actors on the screen.

        Args:
            self (OutputService): An instance of OutputService.
            actors (list): The actors to render.
        """ 
        for actor in actors:
            self.draw_actor(actor)
    
    def flush_buffer(self):
        pygame.display.update()

