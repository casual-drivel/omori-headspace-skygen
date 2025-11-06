import pygame
import notoFillscreen
import notoSpread
import gui

class Engine:
    def __init__(self, mode):
        # Fallbacks
        self.emojis = "🤎🖤💛💚💙✨⭐💫❤︎‍🩹🌟🌙☄" #"🌎️🛌🛰️📖💎🪐🌕️👁️s⭐️"
        self.xRes = 1280
        self.yRes = 1024
        self.mode = mode  # can be 'fillscreen' 'spread'
        self.screenMode = 'windowed'  # can be windowed or fullscreen
        self.redrawNeeded = False
        self.renderingSurface = None  # The pygame surface that will contain the drawn surface

        # important stuff
        self.running = True
        self.screen = pygame.display.set_mode((self.xRes, self.yRes))
        self.clock = pygame.time.Clock()
        self.events = None
        self.noto = None  # the Noto Drawing Library
        self.pygame = pygame  # ?????
        self.pygame.key.set_repeat(0)
        # Program stretches its legs
        self.initFunctions()  # run last or fix noto

    def initFunctions(self):
        '''these start at runtime'''
        if self.mode == 'fillscreen':
            self.notoFillscreen()  # initialize the screenfiller
        elif self.mode == 'spread':
            self.notoSpread()
        pygame.init()  # initialize the library
        pygame.font.init()
        # self.initDisplay() # might be unneeded

    def guiInit(self):
        # given our shoddy architecture, we'll call this during the initial rendering, and not the loop
        self.ui = gui.Gui(self.xRes,self.yRes,self.renderingSurface)
        self.ui.clock = self.clock
        # self.ui.drawButton() # POC to test this works, we really dont need it actually

    def notoFillscreen(self):
        # Used only for the screen filler
        # This ones important because its the actual rendering class being
        # initialized
        self.noto = notoFillscreen.Noto(screen_x=self.xRes,
                                        screen_y=self.yRes,
                                        fontSize=32,
                                        color=(255, 235, 255),
                                        background=(108, 15, 254),
                                        text=self.emojis
                                        )
        # now provides a surface filled with emoji's
        self.noto.emojiArrayInit()
        self.renderingSurface = self.noto.render_advanced()

    def notoSpread(self):
        self.noto = notoSpread.Noto(screen_x=self.xRes,
                                    screen_y=self.yRes,
                                    fontSize=64,
                                    pixelSize=2,
                                    color=(255, 235, 255),
                                    background=(108, 15, 254),
                                    text=self.emojis
                                    )
        self.noto.initFunctions()
        self.renderingSurface = self.noto.renderSplayed()
        self.guiInit()

    def returnDisplay(self):
        return self.screen

    def getMaxResolution(self):
        screen_width, screen_height = pygame.display.get_desktop_sizes()[0]
        return screen_width, screen_height

    def eventHandler(self):
        self.events = pygame.event.get()  # get the events

        # We need to move this elsewhere... later
        for event in self.events:
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:  # or event.type == pygame.KEYUP: # Removed the keyup section
                if event.dict['key'] == pygame.K_p:  # screenshot
                    # print('screenshot taken!')
                    pygame.image.save(self.screen, "example1.png")
                if event.dict['key'] == pygame.K_f:  # fullscreen toggle
                    if self.screenMode == 'windowed':
                        self.screenMode = 'fullscreen'
                        # pygame.display.toggle_fullscreen()
                        self.xRes, self.yRes = self.getMaxResolution()
                        # print(self.getMaxResolution())
                        self.redrawNeeded = True
                        self.screen = pygame.display.set_mode(
                            (self.xRes, self.yRes), pygame.FULLSCREEN)
                    elif self.screenMode == 'fullscreen':
                        self.screenMode = 'windowed'
                        pygame.display.toggle_fullscreen()
                        self.xRes, self.yRes = 1280, 1024
                        self.redrawNeeded = True
                        pygame.display.set_mode(
                            (self.xRes, self.yRes), pygame.RESIZABLE)
            self.ui.processEvent(event)

    # The thing responsible for piecing it all together
    def mainFunction(self):
        if self.mode == 'fillscreen':
            self.screen.fill("black")
            self.screen.blit(self.renderingSurface, (0, 0))
            self.pygame.display.flip()
            if self.redrawNeeded:
                self.notoFillscreen()
                self.redrawNeeded = False
        if self.mode == 'spread':
            self.screen.fill("black")
            self.screen.blit(self.renderingSurface, (0, 0))

            # UI Stuff
            self.ui.processTime()
            self.ui.draw_ui()

            self.pygame.display.flip()
            if self.redrawNeeded:
                self.notoSpread()
                self.redrawNeeded = False
