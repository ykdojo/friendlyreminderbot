# Task: Open reminders.txt, which contains a list of reminders, and print a random one out.
from load_env import load_twitter_env # function for loading keys!
from time import sleep
import random
import tweepy

from yaml import load, dump
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

# Loading twitter credentials
consumer_key, consumer_secret, access_token, access_token_secret, bearer_token = load_twitter_env()

# Connect to the TWITTER Client
client = tweepy.Client(bearer_token=bearer_token,
                       consumer_key=consumer_key, 
                       consumer_secret=consumer_secret, 
                       access_token=access_token, 
                       access_token_secret=access_token_secret)


def remind():
    while True:
        with open('reminders.txt') as f:
            categories = load(f.read(), Loader=Loader)

        reminders_to_print = []
        for subcategory in categories.values():
            for reminders in subcategory.values():
                for reminder_raw_text in reminders:
                    reminders_to_print.append(reminder_raw_text.strip())

        # Random reminder tweets
        reminder = random.choice(reminders_to_print)
        print(reminder)
        client.create_tweet(text=reminder)
        # sleeps for 4 hours
        sleep(14400)


if __name__ == "__main__":
   remind()
