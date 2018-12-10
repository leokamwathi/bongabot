'''
Run the bot in command line.
'''

import re
import random
from live_bot import LiveBot

def main():
    livebot = LiveBot()
    print ("Hello. How are you feeling today?")

    while True:
        statement = input("> ")
        print (livebot.chat(statement))

        if statement == "quit":
            break


if __name__ == "__main__":
    main()