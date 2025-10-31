import pygame


class Events:
    def __init__(self, events):
        self.dummy = 'dummy'
        self.events = events

    def keyHandler(self):
        for event in self.events:
            if event.type == pygame.QUIT:
                return
