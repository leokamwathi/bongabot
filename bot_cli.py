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
        if statement == "quit":
            print("Good bye. I was lovely talking to you.")
            break
        else:
            print (livebot.chat(statement))


if __name__ == "__main__":
    main()