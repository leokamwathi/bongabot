# Python libraries that we need to import for our bot
import random
import re
from flask import Flask, request
from pymessenger.bot import Bot
from live_bot import LiveBot
import os

app = Flask(__name__)
#ACCESS_TOKEN = 'ACCESS_TOKEN'   #
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
#VERIFY_TOKEN = 'VERIFY_TOKEN'   #
VERIFY_TOKEN = os.environ['VERIFY_TOKEN']
bot = Bot(ACCESS_TOKEN)
livebot = LiveBot()

# We will receive messages that Facebook sends our bot at this endpoint

@app.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        """Before allowing people to message your bot, Facebook has implemented a verify token
        that confirms all requests that your bot receives came from Facebook."""
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    # if the request was not get, it must be POST and we can just proceed with sending a message back to user
    else:
        # get whatever message a user sent the bot
        output = request.get_json()
        log(output)

        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                if message.get('message'):
                    # Facebook Messenger ID for user so we know where to send response back to
                    recipient_id = message['sender']['id']
                    send_isTyping(recipient_id)
                    if message['message'].get('text'):

                        if message['message'].get('text') == "file test":
                            send_file(recipient_id)
                        else:
                        response_sent_text = livebot.chat(message['message'].get('text'))
                        send_message(recipient_id, response_sent_text)
                    # if user sends us a GIF, photo,video, or any other non-text item
                    if message['message'].get('attachments'):
                        response_sent_nontext = livebot.chat('something else')
                        send_message(recipient_id, response_sent_nontext)
    return "Message Processed"


def verify_fb_token(token_sent):
    # take token sent by facebook and verify it matches the verify token you sent
    # if they match, allow the request, else return an error
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


# chooses a random message to send to the user
def get_message():
    sample_responses = ["You are stunning!", "We're proud of you.",
                        "Keep on being you!", "We're greatful to know you :)"]
    # return selected item to the user
    return random.choice(sample_responses)

# uses PyMessenger to send response to user


def send_message(recipient_id, response):
    # sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"


def send_file(recipient_id):
    # sends user the text message provided via input response parameter
    bot.send_file_url("")
    return "success"


def send_isTyping(recipient_id):
    # sends user the text message provided via input response parameter
    bot.send_action(recipient_id,'typing_on') #.send_text_message(recipient_id, response)
    return "success"


def log(msg, *args, **kwargs):  # simple wrapper for logging to stdout on heroku
    try:
        if type(msg) is dict:
            msg = json.dumps(msg)
        else:
            msg = unicode(msg).format(*args, **kwargs)
        print (u"{}: {}".format(datetime.now(), msg))
    except UnicodeEncodeError:
        pass  # squash logging errors in case of non-ascii text
    sys.stdout.flush()

if __name__ == "__main__":
    app.run()
