import toml

#Grab The Oauth keys
config = open("config.toml", "r")
config = toml.loads(config.read())

#Import these into app.py
OAUTH_TOKEN = config["OAUTH_TOKEN"]
OAUTH_SECRET = config["OAUTH_SECRET"]
CONSUMER_KEY = config["CONSUMER_KEY"]
CONSUMER_SECRET = config["CONSUMER_SECRET"]
