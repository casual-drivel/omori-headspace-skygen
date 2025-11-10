import pygame
import random
import grapheme

'''library for printing notoemoji wallpapers'''

# Things to Work on

# Add "Depth" to the Emoji ("Squish" the side to make "Perspective")
# For the love of god make this PEP8 Compliant, and Clean up redundancy\
# MAYBE Add "Line squiggler" with OpenCV? (Canny edge detection Maybe)

# All this GUI Stuff should be toggle-able
# ...Add GUI to Control Color(s)
# ...Add Input to take in Emoji's
# ...Size of Emoji and Star Slider
# Matter of fact, lets find a way to just plug everything into a GUI - People love GUI's
# including a save button, I think

# Final goal is we want to be able to host this somehow in a RO S3, or
# lambda, or something


class Noto:
    def __init__(
            self,
            fontSize=64,
            text="🖤🖤❤⬛︎",
            color="white",
            screen_x=1920,
            screen_y=1080,
            background="black",
            pixelSize=16):
        pygame.font.init()
        self.fontSize = fontSize
        self.pixelSize = pixelSize
        self.text = text  # note this is an iterator
        self.color = color
        self.background = background
        self.screen_x = screen_x
        self.screen_y = screen_y

        # used for determine where we draw emojis
        self.percent = 30  # 30%?
        self.emojiArray = [] # the emoji surfaces we'll use for drawing, not the final one
        self.emojiDrawArray = [] # The array we'll use for drawing the emoji's
        self.cell_dict = {}  # AFTER Processing, this is filled with "empty" tile coordinates
        self.emoji_cell_dict_mask = {}  # the random "positions" we selected from cell_dict
        self.padding = 16  # how much padding to add and space out emoji's
        self.degrees = 30
        # ... and the stars
        self.starSize = 4
        self.starfontSet = pygame.font.Font(
            "Resources/NotoEmojiFont/NotoEmoji-Regular.ttf", size=self.starSize)
        self.starDensity = 5
        self.starFontSurfaces = []
        self.starSurfaces = []

        # load the stuff we need
        self.fontSet = pygame.font.Font(
            "Resources/NotoEmojiFont/NotoEmoji-Regular.ttf",
            size=self.fontSize)
        self.initFunctions()

    def initFunctions(self):
        self.defineCells()
        self.surfaceArray()
        self.spaceOutSurface()
        self.starsInit()

    def surfaceArray(self):
        # returns an array of the surfaces, pixelated
        if self.emojiArray:
            self.emojiArray = []
        for emoji in grapheme.graphemes(self.text):  # for each text emoji we have
            surf = self.fontSet.render(text=emoji,
                                       antialias=True,
                                       color=self.color
                                       # bgcolor = self.background
                                       )
            pxl_surf = pygame.transform.pixelate(surf, self.pixelSize)
            self.emojiArray.append(pxl_surf)

    def defineCells(self):
        '''figure out the size of cells based on the font-size'''
        spacing_y = [
            spacing_y for spacing_y in range(
                0,
                self.screen_y,
                self.fontSize +
                self.padding)]
        spacing_x = [
            spacing_x for spacing_x in range(
                0,
                self.screen_x,
                self.fontSize +
                self.padding)]
        # now create an entire dictionary of our array
        for row in spacing_y:
            self.cell_dict[row] = spacing_x.copy()

    def spaceOutSurface(self):
        # Change this function later to "pop" to the mask, so we can draw stars on the leftovers
        # determine "spacing" and "density" of surfaces
        # returns non-overlapping corners to draw surfaces on
        # takes a "percentage", and measures the side of cell_dict[0] array

        cells_to_populate = int((self.percent * .01) * len(self.cell_dict[0]))
        for key in self.cell_dict.keys():  # for each row
            self.emoji_cell_dict_mask[key] = []
            self.emoji_cell_dict_mask[key].extend(
                random.sample(
                    self.cell_dict[key],
                    cells_to_populate))  # pick percentage of cells
            for choice in self.emoji_cell_dict_mask[key]:
                self.cell_dict[key].remove(choice)

            # for choice in self.emoji_cell_dict_mask[key]:
            #     self.cell_dict[key].remove(choice)

            # for cell in range(0,cells_to_populate):
            #     length_of_row = len(self.emoji_cell_dict_mask[key])
            #     self.emoji_cell_dict_mask[key].pop(random.randrange(0,length_of_row-1))

    def spaceOutEmojiArray(self):
        emoji_mask_surfaces = []  # where we'll store our blits

        # Datastructure is [[surface,(x,y)],[surface,(x,y)]]
        # Create the array of emoji's to blit
        for row in self.emoji_cell_dict_mask:
            for position in self.emoji_cell_dict_mask[row]:
                emoji_mask_surfaces.append([self.rotateSurface(
                    random.choice(self.emojiArray), self.degrees), (position, row)])

        self.emojiDrawArray = emoji_mask_surfaces


    def starsInit(self):
        # Initialze the stars we'll use
        # ensure to set sizes, or give choice for random sizes
        if self.starFontSurfaces:
            self.starFontSurfaces = []

        stars = ".'+*`"
        for star in stars:
            self.starFontSurfaces.append(
                self.starfontSet.render(
                    star, True, self.color))

    def drawStars(self):
        # take x,y arguments - the total size of the cell (in font pixels + padding?)
        # pick "density" amount of random pixels - ensure they're spaced out enough
        # draw random stars on those pixels
        # return the surface
        x = self.fontSize + self.padding
        y = x
        # creates a "tile" of size based on font
        tile = pygame.surface.Surface((x, y))
        tile.fill(self.background)  # adjust transparency later
        for density in range(0, self.starDensity):
            randomX = random.randint(0, x)
            randomY = random.randint(0, y)
            tile.blit(random.choice(self.starFontSurfaces), (randomX, randomY))
        return tile

    def starArray(self):
        if self.starSurfaces:
            self.starSurfaces = []
        # for each row and each cell in cell_dict
        # call drawStars(x,y,density)
        # append to starblits list [[surface,(x,y)],[surface,(x,y)]]
        for y in self.cell_dict:  # y is vertical
            for x in self.cell_dict[y]:  # x is horizontal, readability
                self.starSurfaces.append([self.drawStars(), (x, y)])

    # need to rotate surfaces
    def rotateSurface(self, surface, degrees):
        rotationAngle = random.randint(-degrees, degrees)
        # returns a surface
        return pygame.transform.rotate(surface=surface, angle=rotationAngle)

    def renderSplayed(self):
        # this should *ONLY* be doing Rendering
        renderSurface = pygame.surface.Surface((self.screen_x, self.screen_y))
        renderSurface.fill(color=self.background)
        # take the screen resolution as arguments
        # create "len(self.emojis)" amount of surfaces, Pixelate them
        # distort them?
        # fill the screen with "argument" amount of emoji's, randomly askewed
        # add "argument" amount of stars
        # do not overlap

        # populates emojiDrawArray with surfaces for drawing
        self.spaceOutEmojiArray()

        # Populates starSurfaces with surfaces for drawing
        self.drawStars()
        self.starArray()

        # Do the thing
        renderSurface.blits(blit_sequence=self.starSurfaces)
        renderSurface.blits(blit_sequence=self.emojiDrawArray)
        # final step, give the surface, rendered, and ready to be displayed
        return renderSurface

    def updateEmojis(self):
        self.initFunctions()
        self.spaceOutEmojiArray()
        self.starsInit()
        self.drawStars()
        self.starArray()
