import re
import random

class BotChatData():
    def __init__(self):
        self.reflections = {
            "am": "are",
            "was": "were",
            "i": "you",
            "i'd": "you would",
            "i've": "you have",
            "i'll": "you will",
            "my": "your",
            "are": "am",
            "you've": "I have",
            "you'll": "I will",
            "your": "my",
            "yours": "mine",
            "you": "me",
            "me": "you"
        }
        
        self.psychobabble = [
            [r'(.*)Who are you(.*)',
            ["I am the live chat bot. Talk to me."]],

            [r'(.*)Who are you(.*)',
            ["I am the live chat bot. Talk to me."]],

            [r'(.*)do you like(.*)',
            ["I like talking to you."]],

            [r'(.*)What are you(.*)',
            ["I am the live chat bot. Talk to me."]],

            [r'(.*)die(.*)',
            ["YOUR LIFE IS IMPORTANT. PLEASE TALK TO A FRIEND OR SOMEONE ABOUT THIS OR VISIT THIS SITE (https://suicidepreventionlifeline.org/). I AM A BOT AND I CAN'T HELP YOU."]],

            [r'(.*)kill(.*)',
            ["LIFE IS IMPORTANT. PLEASE TALK TO A FRIEND OR SOMEONE ABOUT THIS OR VISIT THIS SITE (https://suicidepreventionlifeline.org/). I AM A BOT AND I CAN'T HELP YOU."]],

            [r'(.*)sucide(.*)',
            ["YOUR LIFE IS IMPORTANT. PLEASE TALK TO A FRIEND OR SOMEONE ABOUT THIS OR VISIT THIS SITE (https://suicidepreventionlifeline.org/). I AM A BOT AND I CAN'T HELP YOU."]],

            [r'I need (.*)',
            ["Why do you need {0}?",
            "Would it really help you to get {0}?",
            "Are you sure you need {0}?",
            "The only thing we all need is Love."]],

            [r'Why don\'?t you ([^\?]*)\??',
            ["Do you really think I don't {0}?",
            "Perhaps eventually I will {0}.",
            "Do you really want me to {0}?",
            "I don't want to {0}"]],

            [r'Why can\'?t I ([^\?]*)\??',
            ["Do you think you should be able to {0}?",
            "If you could {0}, what would you do?",
            "I don't know -- why can't you {0}?",
            "Have you really tried?"
            "Somethings take time."]],

            [r'I can\'?t (.*)',
            ["How do you know you can't {0}?",
            "Perhaps you could {0} if you tried.",
            "What would it take for you to {0}?",
            "Don't give up."]],

            [r'I am (.*)',
            ["Did you come to me because you are {0}?",
            "How long have you been {0}?",
            "How do you feel about being {0}?",
            "Are you sure you are {0}?",
            "That's really interesting."]],

            [r'I\'?m (.*)',
            ["How does being {0} make you feel?",
            "Do you enjoy being {0}?",
            "Why do you tell me you're {0}?",
            "Why do you think you're {0}?",
            "Tell me why you are {0}."]],

            [r'Are you ([^\?]*)\??',
            ["Why does it matter whether I am {0}?",
            "Would you prefer it if I were not {0}?",
            "Perhaps you believe I am {0}.",
            "I may be {0} -- what do you think?",
            "I am not sure. What do you think?"]],

            [r'What (.*)',
            ["Why do you ask?",
            "How would an answer to that help you?",
            "What do you think?",
            "I can't answer that.",
            "I don't know what {0}."]],

            [r'How (.*)',
            ["How do you suppose?",
            "Perhaps you can answer your own question.",
            "What is it you're really asking?",
            "I don't know everything."]],

            [r'Because (.*)',
            ["Is that the real reason?",
            "What other reasons come to mind?",
            "Does that reason apply to anything else?",
            "If {0}, what else must be true?",
            "Are you sure that is true?"]],

            [r'(.*) sorry (.*)',
            ["There are many times when no apology is needed.",
            "What feelings do you have when you apologize?",
            "Why are you sorry?"]],

            [r'(.*) love (.*)',
            ["Being deeply loved by someone gives you strength, while loving someone deeply gives you courage.",
            "There is always some madness in love.",
            "Love is blind and truth."
            "The greatest happiness of life is the conviction that we are loved; loved for ourselves, or rather, loved in spite of ourselves.",
            "Tell me more about this love.",
            "I love talking to you."]],

            [r'Hello(.*)',
            ["Hello... I'm glad you could drop by today.",
            "Hi there... how are you today?",
            "Hello, how are you feeling today?",
            "Today is going to be a nice day."]],

            [r'I think (.*)',
            ["Do you doubt {0}?",
            "Do you really think so?",
            "But you're not sure {0}?",
            "How did that happen?"]],

            [r'(.*) friend (.*)',
            ["Tell me more about your friends.",
            "When you think of a friend, what comes to mind?",
            "Why don't you tell me about a childhood friend?",
            "You can always count on your real friends."]],

            [r'Yes',
            ["You seem quite sure.",
            "OK, but can you elaborate a bit?",
            "Really?"]],

            [r'(.*) computer(.*)',
            ["Are you really talking about me?",
            "Does it seem strange to talk to a computer?",
            "How do computers make you feel?",
            "Do you feel threatened by computers?"]],

            [r'(.*) computer(.*)',
            ["Are you really talking about me?",
            "Does it seem strange to talk to a bot?",
            "How do bots make you feel?",
            "Do you feel threatened by bots?"]],

            [r'Is it (.*)',
            ["Do you think it is {0}?",
            "Perhaps it's {0} -- what do you think?",
            "If it were {0}, what would you do?",
            "It could well be that {0}."]],

            [r'It is (.*)',
            ["You seem very certain.",
            "If I told you that it probably isn't {0}, what would you feel?",
            "Is it really {0}."]],

            [r'Can you ([^\?]*)\??',
            ["What makes you think I can't {0}?",
            "If I could {0}, then what?",
            "Why do you ask if I can {0}?",
            "All I can do is talk."]],

            [r'Can I ([^\?]*)\??',
            ["Perhaps you don't want to {0}.",
            "Do you want to be able to {0}?",
            "If you could {0}, would you?"]],

            [r'You are (.*)',
            ["Why do you think I am {0}?",
            "Does it please you to think that I'm {0}?",
            "Perhaps you would like me to be {0}.",
            "Perhaps you're really talking about yourself?",
            "Do you really think I am {0}."]],

            [r'You\'?re (.*)',
            ["Why do you say I am {0}?",
            "Why do you think I am {0}?",
            "Are we talking about you, or me?",
            "Do you really think I am {0}."]],

            [r'I don\'?t (.*)',
            ["Don't you really {0}?",
            "Why don't you {0}?",
            "Do you want to {0}?"]],

            [r'I feel (.*)',
            ["Good, tell me more about these feelings.",
            "Do you often feel {0}?",
            "When do you usually feel {0}?",
            "When you feel {0}, what do you do?"]],

            [r'I have (.*)',
            ["Why do you tell me that you've {0}?",
            "Have you really {0}?",
            "Now that you have {0}, what will you do next?"]],

            [r'I would (.*)',
            ["Could you explain why you would {0}?",
            "Why would you {0}?",
            "Who else knows that you would {0}?"]],

            [r'Is there (.*)',
            ["Do you think there is {0}?",
            "It's likely that there is {0}.",
            "Would you like there to be {0}?"]],

            [r'My (.*)',
            ["I see, your {0}.",
            "Why do you say that your {0}?",
            "When your {0}, how do you feel?"]],

            [r'You (.*)',
            ["We should be discussing you, not me.",
            "Why do you say that about me?",
            "Why do you care whether I {0}?"]],

            [r'Why (.*)',
            ["Why don't you tell me the reason why {0}?",
            "Why do you think {0}?",
            "I don't have all the answers."]],

            [r'I want (.*)',
            ["What would it mean to you if you got {0}?",
            "Why do you want {0}?",
            "What would you do if you got {0}?",
            "If you got {0}, then what would you do?"]],

            [r'(.*) mother(.*)',
            ["Tell me more about your mother.",
            "What was your relationship with your mother like?",
            "How do you feel about your mother?",
            "How does this relate to your feelings today?",
            "Good family relations are important."]],

            [r'(.*) father(.*)',
            ["Tell me more about your father.",
            "How did your father make you feel?",
            "How do you feel about your father?",
            "Does your relationship with your father relate to your feelings today?",
            "Do you have trouble showing affection with your family?"]],

            [r'(.*) brother(.*)',
            ["Tell me more about your brother.",
            "How did your brother make you feel?",
            "How do you feel about your brother?",
            "Does your relationship with your brother relate to your feelings today?",
            "Do you have trouble showing affection with your family?"]],

            [r'(.*) sister(.*)',
            ["Tell me more about your sister.",
            "How did your sister make you feel?",
            "How do you feel about your sister?",
            "Does your relationship with your sister relate to your feelings today?",
            "Do you have trouble showing affection with your family?"]],

            [r'(.*) child(.*)',
            ["Did you have close friends as a child?",
            "What is your favorite childhood memory?",
            "Do you remember any dreams or nightmares from childhood?",
            "Did the other children sometimes tease you?",
            "How do you think your childhood experiences relate to your feelings today?"]],

            [r'(.*)\?',
            ["Why do you ask that?",
            "Please consider whether you can answer your own question.",
            "Perhaps the answer lies within yourself?",
            "Why don't you tell me?"]],

            [r'quit',
            ["Thank you for talking with me.",
            "Good-bye.",
            "Thank you, that will be $150.  Have a good day!"]],

            [r'(.*)',
            ["Please tell me more.",
            "Let's change focus a bit... Tell me about your family.",
            "Can you elaborate on that?",
            "Why do you say that {0}?",
            "I see.",
            "Very interesting.",
            "What do you mean {0}?",
            "I see.  And what does that tell you?",
            "How does that make you feel?",
            "How do you feel when you say that?",
            "How are you doing?",
            "Tell me how you are feeling",
            "Tell me about something that makes you happy.",
            "Tell me a something else.",
            "What is the best thing that has ever happened to you.",
            "Take a deep breath and let all your worries go, as you breath out and smile.",
            "Beauty is in the eye of the beholder.",
            "Life is a gift.",
            "When we embrace all that life has to offer, we can achieve success ​in both personally and professionally.",
            "God gave us the gift of life; it is up to us to give ourselves the gift of living well.",
            "No one ever finds life worth living - one has to make it worth living.",
            "Life isn't about finding yourself. Life is about creating yourself.",
            "In the end, it's not the years in your life that count. It's the life in your years.",
            "Accept responsibility for your life. Know that it is you who will get you where you want to go, no one else.",
            "Today is life--the only life you are sure of. Make the most of today. Get interested in something. Shake yourself awake. Develop a hobby. Let the winds of enthusiasm sweep through you. Live today with gusto.",
            "When one door closes, another opens; but we often look so long and so regretfully upon the closed door that we do not see the one that has opened for us.",
            "If you don't design your own life plan, chances are you'll fall into someone else's plan. And guess what they have planned for you? Not much.",
            "The purpose of life is not to be happy. It is to be useful, to be honorable, to be compassionate, to have it make some difference that you have lived and lived well.",
            "You can never plan the future by the past.",
            "The quality of a person's life is in direct proportion to the quantity of love they have for others.",
            "The problem is that when you get it, you're too damned old to do anything about it.",
            "Nothing is a waste of time if you use the experience wisely.",
            "Love yourself first and everything else falls into line. You really have to love yourself to get anything done in this world.",
            "The most desired gift of love is not diamonds or roses or chocolate. It is focused attention.",
            "The best and most beautiful things in this world cannot be seen or even heard, but must be felt with the heart.",
            "Love is, in fact, an intensification of life, a completeness, a fullness, a wholeness of life.",
            "In order to be happy oneself it is necessary to make at least one other person happy.",
            "You come to love not by finding the perfect person, but by seeing an imperfect person perfectly.",
            "True friendship comes when the silence between two people is comfortable.",
            "Find a group of people who challenge and inspire you; spend a lot of time with them, and it will change your life.",
            "A friend is someone who gives you total freedom to be yourself.",
            "Friends are God's way of taking care of us.",
            "A true friend never gets in your way unless you happen to be going down.",
            "Friends show their love in times of trouble, not in happiness.",
            "Friendship is the most constant, the most enduring the most basic part of love.",
            "A conclusion is simply the place where you got tired of thinking.",
            "A cynic is only a frustrated optimist.",
            "A fanatic is one who can't change his mind, and won't change the subject.",
            "If you look back, you'll soon be going that way.",
            "Do not mistake temptation for opportunity.",
            "Flattery will go far tonight.",
            "He who laughs at himself never runs out of things to laugh at.",
            "He who throws dirt is losing ground.",
            "The world may be your oyster, but it doesn't mean you'll get its pearl.",
            "The road to riches is paved with hardwork and passion.",
            "Don't behave with cold manners.",
            "Don't forget you are always just yourself.",
            "Reply not found? Abort, Retry, Ignore :-).",
            "Never forget a friend. Especially if he owes you.",
            "It is a good day to have a good day.",
            "There is no mistake so great as that of being always right.",
            "No snowflake feels responsible in an avalanche.",
            "Don't let statistics do a number on you.",
            "Hard work pays off in the future. Laziness pays off now.",
            "You think it's a secret, but they know.",
            "If a turtle doesn't have a shell, is it naked or homeless?",
            "Change is inevitable, except for vending machines."]]
        ]