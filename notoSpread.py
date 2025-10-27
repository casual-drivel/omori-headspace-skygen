import pygame
import random

'''library for printing notoemoji wallpapers'''

class Noto:
    def __init__(self, fontSize=64, text="🖤🖤❤⬛︎", color="white", screen_x=1920, screen_y=1080, background="black",pixelSize = 16):
        self.fontSize = fontSize
        self.pixelSize = pixelSize
        self.text = text
        self.color = color
        self.background = background
        self.screen_x = screen_x
        self.screen_y = screen_y

        # # used for determine where we draw junk
        self.percent = 30 # 30%?
        self.cell_dict = {}
        self.emojiArray = []
        self.emoji_cell_dict_mask = {} # the random "positions" we selected from cell_dict

        # load the stuff we need
        pygame.font.init()
        self.fontSet = pygame.font.Font("NotoEmoji-Regular.ttf", size=self.fontSize)
        # self.fontSet = font.SysFont("NotoEmoji", size=self.fontSize)
        self.initFunctions()

    def initFunctions(self):
        self.defineCells()
        self.surfaceArray()
        self.spaceOutSurface()

    def surfaceArray(self):
        # returns an array of the surfaces, pixelated
        # self.emojiArray
        for emoji in self.text: # for each text emoji we have
            print(emoji)
            surf = self.fontSet.render(text = emoji,
                                       antialias = True,
                                       color = self.color
                                       # bgcolor = self.background
                                       )
            pxl_surf = pygame.transform.pixelate(surf, self.pixelSize)
            self.emojiArray.append(pxl_surf)

    def defineCells(self):
        '''figure out the size of cells based on the font-size'''
        spacing_y = [spacing_y for spacing_y in range(0,self.screen_y,self.fontSize)]
        spacing_x = [spacing_x for spacing_x in range(0,self.screen_x, self.fontSize)]
        # now create an entire dictionary of our array
        for y in spacing_y:
            self.cell_dict[y] = spacing_x

    def spaceOutSurface(self):
        # Change this function later to "pop" to the mask, so we can draw stars on the leftovers
        # determine "spacing" and "density" of surfaces
        # returns non-overlapping corners to draw surfaces on
        # takes a "percentage", and measures the side of cell_dict[0] array

        cells_to_populate = int((self.percent*.01) * len(self.cell_dict[0]))
        for key in self.cell_dict.keys(): # for each row
            self.emoji_cell_dict_mask[key] = []
            self.emoji_cell_dict_mask[key].extend(random.choices(self.cell_dict[key],k=cells_to_populate)) # pick percentage of cells


    # need to rotate surfaces
    def rotateSurfaces(self,surface, degrees):
        rotationAngle = random.randint(-degrees,degrees)
        pygame.transform.rotate(surface = surface, angle = rotationAngle)


    def renderSplayed(self):
        renderSurface = pygame.surface.Surface((self.screen_x,self.screen_y))
        renderSurface.fill(color=self.background)
        # take the screen resolution as arguments
        # create "len(self.emojis)" amount of surfaces, Pixelate them
        # distort them
        # fill the screen with "argument" amount of emoji's, randomly askewed
        # add "argument" amount of stars
        # do not overlap

        emoji_mask_surfaces=[] # where we'll store our blits

        # Datastructure is [[source,(x,y)],[source,(x,y)]]
        for row in self.emoji_cell_dict_mask:
            for position in self.emoji_cell_dict_mask[row]:
                emoji_mask_surfaces.append([random.choice(self.emojiArray),(row,position)]) # Get a random surface

        renderSurface.blits(blit_sequence=emoji_mask_surfaces)

        return renderSurface
