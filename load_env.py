import os
from dotenv import load_dotenv

# takes environment variables from .env
load_dotenv()

def load_twitter_env():
    consumer_key = os.getenv("API_KEY")
    consumer_secret = os.getenv("API_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
    return consumer_key, consumer_secret, access_token, access_token_secret
