
import re
import random
from eliza_chatdata import ElizaChatData



psychobabble = []

def genericResponse():
    global psychobabble
    for pattern, responses in psychobabble:
        #try:
        print(pattern)
        match = re.match(pattern, "what really happened to you.")
        if match:
            response = random.choice(responses)
            try:
                return response.format(" That")
            except:
                pass
        #except:
        #    return "Random2 "
    return ("Exited")

def addChatData(chatdata):
    global psychobabble
    if psychobabble == []:
        psychobabble = chatdata
    else:
        for pattern, responses in chatdata:
            isFound = False
            for patt, resp in psychobabble:
                if pattern == patt:
                    isFound = True
                    for reply in responses:
                        if reply not in resp:
                            resp.append(reply)
            if isFound == False:
                data =[]
                data.append(pattern)
                data.append(responses)
                psychobabble.append(data)


addChatData(ElizaChatData().psychobabble)

print(genericResponse())