import pygame.freetype
from pygame import font
from pygame import surface
import random

'''library for printing notoemoji wallpapers'''

# This one is a neglected Child, but was the POC for me to check feasability of my idea
# i'll show it love


class Noto:
    def __init__(
            self,
            fontSize=12,
            text="🖤🖤❤⬛︎",
            color="white",
            screen_x=1920,
            screen_y=1080,
            background="black"):
        self.fontSize = fontSize
        self.text = text
        self.color = color
        self.background = background
        self.screen_x = screen_x
        self.screen_y = screen_y

        self.emojiArray = []

        # load the stuff we need
        font.init()
        self.fontSet = font.Font(
            "Resources/NotoEmojiFont/NotoEmoji-Regular.ttf",
            size=self.fontSize)
        # self.fontSet = font.SysFont("NotoEmoji", size=self.fontSize)

    def render_simple(self):
        '''simply print 3 default characters, dont define anything else except for Noto to use'''
        return font.Font.render(
            self.fontSet,
            self.text,
            True,
            self.color,
            None)

    def text_jumbler(self):
        '''returns enough emoji's to fill the screen'''
        x_length = int(self.screen_x / self.fontSize) + 50
        if len(self.text) == 1:
            return self.text * x_length

        # if the above isnt true, then split the text string
        # then, randomly fill an array of x_length with the characters
        # combine, then return that array as a string

        textReturn = ''
        textSplit = [x for x in self.text]
        textLen = len(textSplit) - 1
        for x in range(0, x_length):
            textReturn = textReturn + \
                str(textSplit[random.randint(0, textLen)])
        return textReturn

    def emojiArrayInit(self):
        '''initializes the arrays that will store the text for the text jumbler'''
        for y in range(0, self.screen_y, self.fontSize):
            self.emojiArray.append(self.text_jumbler())

    def render_advanced(self):
        textSurface = surface.Surface((self.screen_x, self.screen_y))
        '''takes the resolution, prints emoji's all across the screen'''
        # first figure out how much to go y-wise
        # y_length = int(screen_y/self.fontSize)+4

        # this should be arrays set in the class, that has an entire list of what to print
        # text = self.text_jumbler()
        # fontHolder = font.Font.render(self.fontSet, text, True, self.color, None)
        # for y in range(0,self.screen_y,self.fontSize):
        #     textSurface.blit(fontHolder,(0,y))

        for y in range(0, len(self.emojiArray)):
            fontHold = font.Font.render(
                self.fontSet,
                self.emojiArray[y],
                True,
                self.color,
                self.background)
            textSurface.blit(fontHold, (0, y * self.fontSize))

        return textSurface
