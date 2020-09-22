import tweepy 
import os
import time
def authentication():
  consumer_key=os.getenv("consumer_key")
  consumer_secret=os.getenv("consumer_secret")
  access_token=os.getenv("access_token")
  access_token_secret=os.getenv("access_token_secret")
  
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)
  api = tweepy.API(auth)
  api.verify_credentials()
  print("api created")
  return api

def new_name(user):
  emoji_dict={0:"0️⃣",1:"1️⃣",2:"2️⃣"}
  emoji_list ="".join([emoji_dict[int(i)] for i in str(user.followers_count) if int(i) in emoji_dict.keys()])
  return emoji_list

api = authentication()
while True:
  user = api.get_user("@Chandra34570619")
  api .update_profile(name = f"chandrateja|{new_name(user)}")
  print( f"chandrateja|{new_name(user)}")
  #prev_count_of_followers = user.followers_count
  print("waiting to refresh")
  time.sleep(60)
  
