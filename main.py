from engine import Engine
import asyncio
import grapheme, pygame_gui, i18n, pygame, random, sys, notoSpread, notoFillscreen, gui

engine = Engine('spread')  # can be 'fillscreen' or 'spread'
engine.init_functions()


async def main():

    while engine.running:

        engine.eventHandler()  # Handle the ongoing events
        engine.mainFunction()  # run the main rendering function
        engine.clock.tick(60)
        await asyncio.sleep(0)

    # engine.pygame.quit()
    if not engine.running:
        return

if __name__ == "__main__":
    asyncio.run(main())
