from twitter import *
from Tkinter import *


 
twitter = Twitter(
              auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET,
	                       CONSUMER_KEY, CONSUMER_SECRET)
	           )
 

class App:
 
    def __init__(self, master):
        global textStatus
        frame = Frame(master)
        frame.pack()

        textStatus = StringVar()
        self.statusEntry = Entry(frame, textvariable=textStatus)
        self.statusEntry.pack()
 
        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)
 
        self.Tweet = Button(frame, text="Tweet", command=self.tweet)
        self.Tweet.pack(side=LEFT)
 
    def tweet(self):
        twitter.statuses.update(status=textStatus)
 
root = Tk()
app = App(root)
 
root.mainloop()
