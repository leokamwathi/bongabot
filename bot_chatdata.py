import re
import random
from psych_chatreflections import PsychChatReflections
from psych_chatdata import PsychoChatData
from love_chatdata import LoveChatData
from philo_chatdata import PhiloChatData
class BotChatData():
    
    def __init__(self):
        self.reflections = PsychChatReflections().reflections
        self.psychobabble = []
        self.addChatData(PsychoChatData().psychobabble)
        self.addChatData(LoveChatData().psychobabble)
        self.addChatData(PhiloChatData().psychobabble)

    def addChatData(self,chatdata):
        if self.psychobabble == []:
            self.psychobabble = chatdata
        else:
            for pattern, responses in chatdata:
                isFound = False
                for patt, resp in self.psychobabble:
                    if pattern == patt:
                        isFound = True
                        for reply in responses:
                            if reply not in resp:
                                resp.append(reply)
                if isFound == False:
                    data =[]
                    data.append(pattern)
                    data.append(responses)
                    self.psychobabble.append(data)
