import pygame
import pygame_gui
from i18n.translations import container


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
        self.uiContainer = None
        self.uiVisible = True
        self.uiElements = {}

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
    #     # MUDADA
    #     # WRYYY
    #     pass

    def processEvent(self,event):
        # plugs into event handler
        self.manager.process_events(event)

    def processTime(self):
        # plugs into an appropriate place to process time in the live rendering loop
        time_delta=self.clock.tick(60)/1000.0
        self.manager.update(time_delta)


    def slider(self, name, x,y):
        self.uiElements[name] = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect((x+80, y), (200, 30)),
            container = self.uiContainer,
            start_value= 125,
            value_range=(0,255),
            manager=self.manager,
            parent_element=self.uiContainer
        )

        label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((x,y),(x+80, 30)),
            text=name,
            container=self.uiContainer,
            # parent_element=self.uiElements,
            manager=self.manager
        )

    def uiContainerInit(self):
        self.uiContainer = pygame_gui.elements.UIWindow(
            rect = pygame.Rect((300,300),(300,300)),
            manager=self.manager,
            window_display_title="Stuff Picker",
            resizable=True
        )

        # The actual junk that gets drawn
        self.slider("Red",0,0)
        self.slider("Blue", 0, 30)
        self.slider("Green", 0, 60)

    def toggleUI(self):
        self.uiVisible = not self.uiVisible # toggle if called
        if self.uiVisible:
            # Show it
            self.uiContainer.show()
            print(self.uiElements['Red'].get_current_value())
        else:
            # Hide it
            self.uiContainer.hide()
            pass


    def draw_ui(self):
        # Does the needful, put in rendering loop with the time
        self.manager.draw_ui(self.mainSurface)


