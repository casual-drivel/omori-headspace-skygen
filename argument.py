import argparse

class arghandler:
    '''class to handle arguments'''
    def __init__(self):
        self.parser = argparse.ArgumentParser(
        prog="Noto Emoji Wallpaper Generator",
        description="Generates wallpapers based on arguments",
    )
        self.parser.add_argument('-r','--resolution')
        self.parser.add_argument('-e','--emojis')
        self.parser.add_argument('-c','--color')
        self.parser.add_argument('-b','--background')
        self.parser.add_argument('-s','--scheme')

        self.args = self.parser.parse_args()

        # should only be args color+bg or scheme
        if self.args.color:
            if args.background:
                if args.scheme:
                    print("cannot define both a color/bg and a scheme! Exiting!")
                    exit()
                pass
            elif args.scheme:
                print("cannot define both a color/bg and a scheme! Exiting!")
                exit()

        # if scheme isnt defined, then just keep onwards