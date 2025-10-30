import pygame
import random
import grapheme

'''library for printing notoemoji wallpapers'''

# Bugs to patch
# - Finish "rotation" function, ensure each rotation is a new surface
# - Add "stars" afterwards


class Noto:
    def __init__(self, fontSize=64, text="🖤🖤❤⬛︎", color="white", screen_x=1920, screen_y=1080, background="black",pixelSize = 16):
        pygame.font.init()
        self.fontSize = fontSize
        self.pixelSize = pixelSize
        self.text = grapheme.graphemes(text) # note this is an iterator
        self.color = color
        self.background = background
        self.screen_x = screen_x
        self.screen_y = screen_y

        # used for determine where we draw emojis
        self.percent = 30 # 30%?
        self.emojiArray = []
        self.cell_dict = {} # AFTER Processing, this is filled with "empty" tile coordinates
        self.emoji_cell_dict_mask = {} # the random "positions" we selected from cell_dict
        self.padding = 16 # how much padding to add and space out emoji's
        self.degrees = 30
        # ... and the stars
        self.starSize = 4
        self.starfontSet = pygame.font.Font("NotoEmoji-Regular.ttf", size=self.starSize)
        self.starDensity = 5
        self.starSurfaces = []

        # load the stuff we need
        self.fontSet = pygame.font.Font("NotoEmoji-Regular.ttf", size=self.fontSize)
        # self.fontSet = font.SysFont("NotoEmoji", size=self.fontSize)
        self.initFunctions()

    def initFunctions(self):
        self.defineCells()
        self.surfaceArray()
        self.spaceOutSurface()
        self.starsInit()

    def surfaceArray(self):
        # returns an array of the surfaces, pixelated
        # self.emojiArray
        for emoji in self.text: # for each text emoji we have
            # print(emoji)
            surf = self.fontSet.render(text = emoji,
                                       antialias = True,
                                       color = self.color
                                       # bgcolor = self.background
                                       )
            pxl_surf = pygame.transform.pixelate(surf, self.pixelSize)
            self.emojiArray.append(pxl_surf)

    def defineCells(self):
        '''figure out the size of cells based on the font-size'''
        spacing_y = [spacing_y for spacing_y in range(0,self.screen_y,self.fontSize+self.padding)]
        spacing_x = [spacing_x for spacing_x in range(0,self.screen_x, self.fontSize+self.padding)]
        # now create an entire dictionary of our array
        for row in spacing_y:
            self.cell_dict[row] = spacing_x.copy()

    def spaceOutSurface(self):
        # Change this function later to "pop" to the mask, so we can draw stars on the leftovers
        # determine "spacing" and "density" of surfaces
        # returns non-overlapping corners to draw surfaces on
        # takes a "percentage", and measures the side of cell_dict[0] array

        cells_to_populate = int((self.percent*.01) * len(self.cell_dict[0]))
        for key in self.cell_dict.keys(): # for each row
            self.emoji_cell_dict_mask[key] = []
            self.emoji_cell_dict_mask[key].extend(random.sample(self.cell_dict[key],cells_to_populate)) # pick percentage of cells
            for choice in self.emoji_cell_dict_mask[key]:
                self.cell_dict[key].remove(choice)


            # for choice in self.emoji_cell_dict_mask[key]:
            #     self.cell_dict[key].remove(choice)

            # for cell in range(0,cells_to_populate):
            #     length_of_row = len(self.emoji_cell_dict_mask[key])
            #     self.emoji_cell_dict_mask[key].pop(random.randrange(0,length_of_row-1))

    def starsInit(self):
        # Initialze the stars we'll use
        # ensure to set sizes, or give choice for random sizes
        stars = ".'+*`"
        for star in stars:
            self.starSurfaces.append(self.starfontSet.render(star,True,self.color))

    def drawStars(self,x,y):
        # take x,y arguments - the total size of the cell (in font pixels + padding?)
        # pick "density" amount of random pixels - ensure they're spaced out enough
        # draw random stars on those pixels
        # return the surface
        tile = pygame.surface.Surface((x,y)) # creates a "tile" of size
        for density in range(0,self.starDensity):
            randomX = random.randint(0,x)
            randomY = random.randint(0,y)
            tile.blit(random.choice(self.starSurfaces),(randomX,randomY))
        return tile

    def starArray(self):
        pass
        # for each row and each cell in cell_dict
        # call drawStars(x,y,density)
        # append to starblits list [[surface,(x,y)],[surface,(x,y)]]

    # need to rotate surfaces
    def rotateSurface(self,surface, degrees):
        rotationAngle = random.randint(-degrees,degrees)
        # returns a surface
        return pygame.transform.rotate(surface = surface, angle = rotationAngle)

    # def rotatedSurfaces(self):
    #     rotated_emoji_surfaces = []
    #     for row in self.emoji_cell_dict_mask:
    #         for position in self.emoji_cell_dict_mask[row]:
    #             self.rotateSurface()
    #         rotated_emoji_surfaces.append()


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

        # Datastructure is [[surface,(x,y)],[surface,(x,y)]]
        # Create the array of emoji's to blit
        for row in self.emoji_cell_dict_mask:
            for position in self.emoji_cell_dict_mask[row]:
                emoji_mask_surfaces.append([
                    self.rotateSurface(random.choice(self.emojiArray), self.degrees),(position,row)
                ])

        # Do the thing
        renderSurface.blits(blit_sequence=emoji_mask_surfaces)
        # final step, give the surface, rendered, and ready to be displayed
        return renderSurface
