import toml
from twitter import *
from Tkinter import *

config = open("config.toml", "r")
config = toml.loads(config.read())

OAUTH_TOKEN = config["OAUTH_TOKEN"]
OAUTH_SECRET = config["OAUTH_SECRET"]
CONSUMER_KEY = config["CONSUMER_KEY"]
CONSUMER_SECRET = config["CONSUMER_SECRET"]

twitter = Twitter(
              auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET,
	                       CONSUMER_KEY, CONSUMER_SECRET)
	           )

class App:
 
    def __init__(self, master):
        global tweet
        frame = Frame(master)
        frame.pack()

        tweet = StringVar()
        self.statusEntry = Entry(frame, textvariable=tweet)
        self.statusEntry.pack()
 
        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)
 
        self.Tweet = Button(frame, text="Tweet", command=self.tweet)
        self.Tweet.pack(side=LEFT)
 
    def tweet(self):
        twitter.statuses.update(status=tweet.get())

root = Tk()
app = App(root)
root.mainloop()