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
        self.defaultValues = {}

        # Extra Credit
        ## RAINBOW Mode
        ## "Holographic" Mode triggered by mouse (think shiny pokemon card)
        ## Custom Emojis and Stars


    #     # Not really Needed Here
    #     self.initGui()

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
    def guiButton(self, name, x, linePos):
        self.uiElements[name] = pygame_gui.elements.ui_button.UIButton(
            relative_rect= pygame.Rect((x,linePos),(60,30)),
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


    def slider(self, name, startrange, endrange, linePos, *, start_value = 1):
        # How many pixels between the endlength of the label and beginning of slider
        posX = 0
        textPixelSeperation = posX + 100

        self.uiElements[name] = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect((textPixelSeperation, linePos), (240, 30)), # (240,30) = (width, height) of slider
            container = self.uiContainer,
            start_value = start_value,
            value_range=(startrange, endrange),
            manager=self.manager,
            parent_element=self.uiContainer
        )

        label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((posX, linePos), (textPixelSeperation, 30)), # (width, height) of text
            text=name,
            container=self.uiContainer,
            # parent_element=self.uiElements,
            manager=self.manager
        )

    def labelOnly(self, name, posX, linePos):
        self.uiElements[name] = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((posX, linePos), (len(name)*8, 30)), # multiply by 8 per character
            text=name,
            container=self.uiContainer,
            manager = self.manager
        )

    def uiContainerInit(self):
        line = 30 # little thing to help understand where the line is, max lines, manual

        self.uiContainer = pygame_gui.elements.UIWindow(
            rect = pygame.Rect((300,300),(360,line*19)),
            manager=self.manager,
            window_display_title="Stuff Picker",
            resizable=True
        )

        # The actual elements that gets drawn
        self.textEntryBox("Emojis",0 ,line*0)
        # pass in the default emojis, limit this to only emoji's later
        self.uiElements['Emojis'].set_text(self.defaultEmojis)
        self.guiButton("Redraw", 230,line*0)
        # needs range and label? bg color slider
        self.labelOnly('Emoji Settings',0,line*1)
        self.slider("Emoji Red",0,255, line*2,start_value=255)
        self.slider("Emoji Green", 0,255, line*3,start_value=255)
        self.slider("Emoji Blue", 0,255, line*4,start_value=235)
        self.slider("Emoji Size",0,200, line*5,start_value=64)
        self.slider("Emoji Density",0,100, line*6,start_value=30)
        self.slider("Emoji Rotation",0,360, line*7,start_value=30)
        self.slider("Emoji Spacing",0,100, line*8,start_value=16)
        # size, density, rotation x2 spacing(emoji only)
        self.labelOnly('Star Settings',0,line*9)
        self.slider("Star Red",0,255, line*10,start_value=255)
        self.slider("Star Green", 0,255, line*11,start_value=255)
        self.slider("Star Blue", 0,255, line*12,start_value=235)
        self.slider("Star Size",0,20, line*13,start_value=10) #
        self.slider("Star Density",0,20, line*14,start_value=5)
        # Background
        self.slider("Bg Red",0,255, line*15,start_value=108)
        self.slider("Bg Green", 0,255, line*17,start_value=15)
        self.slider("Bg Blue", 0,255, line*16,start_value=254)
        # duplicate for text, lower

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


