import pygame
from engine import Engine


# imports notoemoji ttf file
# from there, load a provided "list" of emoji's
# set the pygame window size
# arrange the emoji's randomly until the screen is filled

# argparse should take the following
# resolution, emojis, color, background, scheme (cant be mixed)

# FEATURES TO ADD
# line-squiggler
# space out randomly
# amount of stars
# star size variation
# emoji-picker

engine=Engine('spread') # can be 'fillscreen' or 'spread'
engine.initFunctions()
# xRes, yRes = engine.getMaxResolution()


while engine.running:

    engine.eventHandler() # Handle the ongoing events
    engine.mainFunction() # run the main rendering function
    engine.clock.tick(60)

engine.pygame.quit()