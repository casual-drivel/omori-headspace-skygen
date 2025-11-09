import pygame
import pygame_gui
from i18n.translations import container


class Gui:
    def __init__(self, screenX, screenY, defaultEmojis, mainSurface):
        # We will need...
        # screen resolution
        # this is really just a wrapper for the gui library
        # we could probably actually get rid of some of these functions ans just call the mgr

        self.screenX = screenX
        self.screenY = screenY
        self.manager = pygame_gui.UIManager((self.screenX, self.screenY), 'Resources/fontSettings.json')

        # These should be handed in by the running app
        self.clock = None
        # self.event = None
        self.mainSurface = mainSurface
        self.uiContainer = None
        self.uiVisible = True
        self.uiElements = {}
        self.elementValues = {}
        self.defaultEmojis = defaultEmojis

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
    #     self.loadFont()
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

    # Button to initiate Redraw
    def guiButton(self, name, x, y):
        self.uiElements[name] = pygame_gui.elements.ui_button.UIButton(
            relative_rect= pygame.Rect((x,y),(60,30)),
            container = self.uiContainer,
            manager = self.manager,
            text=name
        )

    # Text input for Emojis
    def textEntryBox(self, name, x, y):
        self.uiElements[name] = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(
            relative_rect = pygame.Rect((x+60,y),(170,30)),
            container = self.uiContainer,
            manager = self.manager,
            object_id = "defaults"
        )

        label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((x,y),(x+60, 30)),
            text=name,
            container=self.uiContainer,
            # parent_element=self.uiElements,
            manager=self.manager
        )


    def slider(self, name, x,y):
        self.uiElements[name] = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect((x+60, y), (230, 30)),
            container = self.uiContainer,
            start_value = 125,
            value_range=(0, 255),
            manager=self.manager,
            parent_element=self.uiContainer
        )

        label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((x,y),(x+60, 30)),
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

        # The actual elements that gets drawn
        self.textEntryBox("Emojis",0 ,0)
        # pass in the default emojis, limit this to only emoji's later
        self.uiElements['Emojis'].set_text(self.defaultEmojis)

        self.guiButton("Redraw", 230,0)
        self.slider("Red",0,30)
        self.slider("Blue", 0, 60)
        self.slider("Green", 0, 90)

    def getValues(self):
        # Dump the values we need
        for key in self.uiElements:
            # checks if element is entry line, gets value
            if isinstance(self.uiElements[key], pygame_gui.elements.ui_text_entry_line.UITextEntryLine):
                self.elementValues[key] = self.uiElements[key].get_text()
            # checks if element is slider, gets value
            if isinstance(self.uiElements[key], pygame_gui.elements.UIHorizontalSlider):
                self.elementValues[key] = self.uiElements[key].get_current_value()

        # we end up with something like {'Emojis': '', 'Red': 125, 'Blue': 125, 'Green': 125}


    def toggleUI(self):
        self.uiVisible = not self.uiVisible # toggle if called
        if self.uiVisible:
            # Show it
            self.uiContainer.show()
            # self.getValues() # used for testing
        else:
            # Hide it
            self.uiContainer.hide()
            pass


    def draw_ui(self):
        # Does the needful, put in rendering loop with the time
        self.manager.draw_ui(self.mainSurface)


