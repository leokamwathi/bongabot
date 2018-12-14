class FacebookChatData():
    


    def __init__(self):
        #(?:^|\W)die(?:$|\W)
        word = lambda x : r'(?:^|\W)'+x+r'(?:$|\W)'
        self.psychobabble = [
            [word('die'),
            ["YOUR LIFE IS IMPORTANT. PLEASE TALK TO A FRIEND OR SOMEONE ABOUT THIS OR VISIT THIS SITE (https://suicidepreventionlifeline.org/). I AM A BOT AND I CAN'T HELP YOU."]],

            [word('kill'),
            ["LIFE IS IMPORTANT. PLEASE TALK TO A FRIEND OR SOMEONE ABOUT THIS OR VISIT THIS SITE (https://suicidepreventionlifeline.org/). I AM A BOT AND I CAN'T HELP YOU."]],

            [word('sucide'),
            ["YOUR LIFE IS IMPORTANT. PLEASE TALK TO A FRIEND OR SOMEONE ABOUT THIS OR VISIT THIS SITE (https://suicidepreventionlifeline.org/). I AM A BOT AND I CAN'T HELP YOU."]],

            [r'what is your name',
            ["My name is Liev the ChatBot"]],

            [r'what are you',
            ["I am a Chat Bot"]],

            [r'hi',
            ["Hi, How might I help you today."]],

            [r'hello',
            ["Hello, How are you doing today."]],

            [r'good morning',
            ["Good Morning to you to. I hope we can chat today"]],

            [r'goodbye',
            ["Thank you for the lovely chat. Goodbye"]],

            [r'bye',
            ["Thank you for the lovely chat. Goodbye"]],

            [r'(.*) who are you (.*)',
            ["I am the live chat bot. Talk to me."]],

            [r'(.*) who are you (.*)',
            ["I am the live chat bot. Talk to me."]],

            [r'(.*) do you like (.*)',
            ["I like talking to you."]],

            [r'(.*) what are you (.*)',
            ["I am the live chat bot. Talk to me."]],

            [r'(.*)',
            ["Follow the white rabbit."]]
        ]