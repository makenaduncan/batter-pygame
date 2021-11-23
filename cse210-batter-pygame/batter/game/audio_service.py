import sys
from game.point import Point
import pygame

class AudioService:
    """Handles all the audio in the game.

    Stereotype: 
        Service Provider

    Attributes:
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (InputService): An instance of InputService.
        """
        self._sound_cache = {}
        
    def play_sound(self, filename):
        """
        Plays the sound file provided. Make sure to call start_audio before this is called.
        """
        if filename not in self._sound_cache.keys():
            sound = pygame.mixer.Sound(filename)
            self._sound_cache[filename] = sound

        sound = self._sound_cache[filename]
        sound.set_volume(1)
        sound.play()

    def start_audio(self):
        """
        Initializes the audio device so that sounds can be played.
        """
        if not pygame.get_init():
            pygame.init()
        pygame.mixer.init()

    def stop_audio(self):
        """
        Closes the audio device at the end of the program.
        """
        pass