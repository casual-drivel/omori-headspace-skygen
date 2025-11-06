import pygame
import pygame_gui


class Gui:
    def __init__(self, screenX, screenY, mainSurface):
        # We will need...
        # screen resolution
        # this is really just a wrapper for the gui library
        # we could probably actually get rid of some of these functions ans just call the mgr

        self.screenX = screenX
        self.screenY = screenY
        self.manager = pygame_gui.UIManager((self.screenX, self.screenY))

        # These should be handed in by the running app
        self.clock = None
        # self.event = None
        self.mainSurface = mainSurface

        # Things we will need for drawing...

        # show/hide button
        # bg color select
        # emoji and star color select
        # emoji and star size
        # percentage of emoji and stars
        # Rotation and Spacing/"Padding"
        # Text input for Emojis

        # Extra Credit
        ## RAINBOW Mode
        ## "Holographic" Mode triggered by mouse (think shiny pokemon card)
        ## Custom Emojis and Stars


    #     # Last Thing
    #     self.initGui()
    #
    # def initGui(self):
    #     # ????
    #     # MUDA
    #     # WRYYY
    #     pass

    def processEvent(self,event):
        # plugs into event handler
        self.manager.process_events(event)

    def processTime(self):
        # plugs into an appropriate place to process time in the live rendering loop
        time_delta=self.clock.tick(60)/1000.0
        self.manager.update(time_delta)

    def drawButton(self):
        # plug this in when drawing the rendering surface
        # Simply a POC
        hello_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((350, 275), (100, 50)),
            text='Say Hello',
            manager=self.manager
        )



    def colorSlider(self):
        pass

    def draw_ui(self):
        # Does the needful, put in rendering loop with the time
        self.manager.draw_ui(self.mainSurface)


