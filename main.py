# Task: Open reminders.txt, which contains a list of reminders, and print a random one out.
import os
from load_env import load_twitter_env # function for loading keys!
from time import sleep
import random
import tweepy


# Loading twitter credentials
consumer_key, consumer_secret, access_token, access_token_secret = load_twitter_env()


# Authenticate to Twitter using Tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Connect to the TWITTER API
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

def reminder():
   while True:
     with open('reminders.txt') as f: lines = f.readlines()
     
     # Select a random line from the reminders file.
     lines = [line[1:] for line in lines if line[0] == "-"]
     line = lines[random.randint(0, len(lines) - 1)]
     remind = line.strip()
    
     # Random reminder tweets 
     api.update_status(status=remind)
     # sleeps for 4 hours
     sleep(14400)

if __name__ == "__main__":
   reminder()
