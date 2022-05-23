import os
from dotenv import dotenv_values

# takes environment variables from .env
config = dotenv_values(".env")

def load_twitter_env():
    consumer_key = config["API_KEY"]
    consumer_secret = config["API_SECRET"]
    access_token = config["ACCESS_TOKEN"]
    access_token_secret = config["ACCESS_TOKEN_SECRET"]
    bearer_token = config["BEARER_TOKEN"]
    return consumer_key, consumer_secret, access_token, access_token_secret, bearer_token
