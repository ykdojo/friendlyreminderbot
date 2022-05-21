# Task: Open reminders.txt, which contains a list of reminders, and print a random one out.
import os
from load_env import load_twitter_env # function for loading keys!
from time import sleep
import random
import tweepy

# Loading twitter credentials
consumer_key, consumer_secret, access_token, access_token_secret = load_twitter_env()

# Connect to the TWITTER Client
client = tweepy.Client(bearer_token='enter-token',
                       consumer_key=consumer_key, 
                       consumer_secret=consumer_secret, 
                       access_token=access_token, 
                       access_token_secret=access_token_secret)
def reminder():
   while True:
     with open('reminders.txt') as f: lines = f.readlines()

     # Select a random line from the reminders file.
     lines = [line[3:] for line in lines if len(line) > 2 and line[2] == "-"]
     line = lines[random.randint(0, len(lines) - 1)]
     remind = line.strip()
    
     # Random reminder tweets 
     # client.create_tweet(text=remind)
     print(remind)
     # sleeps for 4 hours
     sleep(14400)

if __name__ == "__main__":
   reminder()
