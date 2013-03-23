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
        global post
        self.frame = Frame(master)
        self.frame.pack()

        #Tweet
        post = StringVar()
        self.tweet = Label(self.frame, wraplength=260)
        self.tweet['textvariable'] = post
        self.tweet.pack()

        #Refresh Button
        self.refresh = Button(self.frame, text="Refresh", fg="blue", command=self.update)
        self.refresh.pack(side=RIGHT)

        #Quit Button
        self.button = Button(self.frame, text="QUIT", fg="red", command=self.frame.quit)
        self.button.pack(side=LEFT)

    def update(self):
        tweets = t.statuses.home_timeline()
        tweet = tweets[0]['user']['screen_name'] + ': ' + tweets[0]['text']
        post.set(tweet)

root = Tk()
app = App(root)
root.mainloop()