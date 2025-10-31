import pygame
# import pygame_widgets
# from pygame_widgets.slider import Slider


class gui:
    def __init__(self):
        self.red = 128
        self.blue = 128
        self.green = 128
        self.alpha = 100
        # 0,0 should be relative to surface
        self.rect = pygame.Rect((0, 0), (200, 100))

        # total size of our drawing space
        self.surface = pygame.Surface((200, 100))
        self.slider_surface = pygame.Surface((800, 40))

    # manually define slider
    # should have the following
    # rectangle, line+selector *3
    # needs to be able to catch event
    def colorpicker(self):
        # rectangle is 100x400
        pygame.draw.rect(
            self.surface,
            (self.red,
             self.green,
             self.blue,
             self.alpha),
            self.rect)
        return self.surface  # return the surface we drew on

    # def sliderTest(self, surface):
    #     slider = Slider(surface, 100, 100, 800, 40, min=0, max=99, step=1)
