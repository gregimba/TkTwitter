from config import OAUTH_SECRET, OAUTH_TOKEN,CONSUMER_KEY,CONSUMER_SECRET
from twitter import *
from Tkinter import *

global t


t = Twitter(
    auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET,
               CONSUMER_KEY, CONSUMER_SECRET)
)

class App:
 
    def __init__(self, master):
        global tweet
        frame = Frame(master)
        frame.pack()

        #Tweet Entry
        tweet = StringVar()
        self.statusEntry = Entry(frame, textvariable=tweet)
        self.statusEntry.pack()

        #Quit
        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

        #Post Tweet
        self.Tweet = Button(frame, text="Tweet", command=self.tweet)
        self.Tweet.pack(side=LEFT)
 
    def tweet(self):
        t.statuses.update(status=tweet.get())
        tweet.set('')

root = Tk()
app = App(root)
root.mainloop()