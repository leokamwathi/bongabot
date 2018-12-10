
import re
import random
from bot_chatdata import BotChatData

class LiveBot():
    def __init__(self):
        #self.chatdata = BotChatData()
        self.reflections = BotChatData().reflections
        self.psychobabble = BotChatData().psychobabble

    def reflect(self,fragment):
        tokens = fragment.lower().split()
        for i, token in enumerate(tokens):
            if token in self.reflections:
                tokens[i] = self.reflections[token]
        return ' '.join(tokens)


    def chat(self,statement):
        for pattern, responses in self.psychobabble:
            match = re.match(pattern, statement.rstrip(".!"))
            if match:
                response = random.choice(responses)
                return response.format(*[self.reflect(g) for g in match.groups()])