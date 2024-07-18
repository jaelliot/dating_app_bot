from bots.tinder_bot import TinderBot
# from bots.bumble_bot import BumbleBot
# from bots.hinge_bot import HingeBot
from time import sleep

def main():
    bot = TinderBot()
    bot.open_app()
    sleep(10)
    bot.auto_swipe()
    bot.send_messages_to_matches()
    bot.close()

if __name__ == "__main__":
    main()
