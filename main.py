from engine import Engine
import asyncio
import grapheme, pygame_gui, i18n

async def main():

    engine = Engine('spread')  # can be 'fillscreen' or 'spread'
    engine.initFunctions()

    while engine.running:

        engine.eventHandler()  # Handle the ongoing events
        engine.mainFunction()  # run the main rendering function
        engine.clock.tick(60)
        await asyncio.sleep(0)

    engine.pygame.quit()

if __name__ == "__main__":
    asyncio.run(main())