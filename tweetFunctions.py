import os
from dotenv import load_dotenv
import tweepy

load_dotenv()
def getClient():
    client = tweepy.Client(bearer_token=os.getenv("bearer_token"), 
                           consumer_key=os.getenv("api_key"),
                           consumer_secret=os.getenv("api_key_secret"), 
                           access_token=os.getenv("access_token"), 
                           access_token_secret=os.getenv("access_token_secret"),)
    return client


def createTweet(reply):
    client = getClient()

    createTweet = client.create_tweet(direct_message_deep_link=None,
                                      for_super_followers_only=None,
                                      place_id=None, media_ids=None,
                                      media_tagged_user_ids=None, 
                                      poll_duration_minutes=None, 
                                      poll_options=None, 
                                      quote_tweet_id=None, 
                                      exclude_reply_user_ids=None, 
                                      in_reply_to_tweet_id=None, 
                                      reply_settings=None, 
                                      text=f"Byte Buddy: {reply}", 
                                      user_auth=True)
    return createTweet

def deleteTweet():
    client = getClient()

    deleteTweet = client.delete_tweet(id="", user_auth= True)

    return deleteTweet

