#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 18:11:43 2018

@author: charles
"""

import tweepy
import glob
import random
import os
import time

from credentials import * 

random.seed(time.time())

#create an OAuthHandler instance
# Twitter requires all requests to use OAuth for authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 

auth.set_access_token(access_token, access_secret)

#Construct the API instance
api = tweepy.API(auth) # create an API object
#api.update_status('Class Time Baby~~~~'    

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
    
def randomimagetwitt(folder):
    #Takes the folder where your images are as the input and twitts one random file.
    images = glob.glob("../" + folder + "/*")
    print(images)
    image_open = images[random.randint(0,len(images)-1)]
    api.update_with_media(image_open)
    
def get_last_tweet(self):
    tweet = self.client.user_timeline(id = self.client_id, count = 1)[0]
    print(tweet.text)  

'''    
def tweetID_Favorite(user_ID):
    tweets = []
    List1 = []
    for tweet in tweepy.Cursor(api.user_timeline,id = user_ID).items():
        tweets.append(tweet)
  
    print("hi charles")
        
    print(tweets[0].id)   

    print("bye charles") 
    for i in tweets: 
        List1.append(i.id) 
        
    num = len(List1) - 1 

    tweetIn = api.get_status(num)
    return int(tweetIn.favorite_count)  

def tweetID_Retweet(user_ID):
    tweets = []
    List1 = []
    for tweet in tweepy.Cursor(api.user_timeline,id = user_ID).items():
        tweets.append(tweet)
  
    print("hi charles")
        
    print(tweets[0].id)   

    print("bye charles") 
    for i in tweets: 
        List1.append(i.id) 
        
    num = len(List1) - 1 

    tweetIn = api.get_status(num)
    return int(tweetIn.retweet_count)  
    
'''

user_id = 'SumTingWongbot' 
numOptions = 0     
i = 0
counter = 0

filename=open('twitterbot.txt','r') 
f=filename.readlines()
filename.close()

api.update_status(f[i])
time.sleep(45)

tweets = []
List1 = []

for tweet in tweepy.Cursor(api.user_timeline,id = user_id).items():
    tweets.append(tweet)
  
print("hi charles")
        
print(tweets[0].id)   

print("bye charles") 

for i in tweets: 
    List1.append(i.id) 
    
tweetIn = api.get_status(List1[0])
print(tweetIn.retweet_count)
print(tweetIn.favorite_count)

num1 = numOptions+1
num2 = numOptions+2
lvl = 0 
    
if (int(tweetIn.retweet_count) > int(tweetIn.favorite_count)):
    api.update_status(f[num2])
    lvl += 2 
elif int(tweetIn.retweet_count) < int(tweetIn.favorite_count):
     api.update_status(f[num1])
     lvl += 1


#get_last_tweet(SumTingWongBot)

    
time.sleep(45) 

tweets1 = [] 
List2 = [] 

for tweet in tweepy.Cursor(api.user_timeline,id = user_id).items():
    tweets1.append(tweet)  
  
print("hi charles")  
        
print(tweets1[0].id)   

print("bye charles") 

for i in tweets: 
    List2.append(i.id) 
    
tweetIn = api.get_status(List2[0])
print(tweetIn.retweet_count)
print(tweetIn.favorite_count)

if lvl == 1:
    if (int(tweetIn.retweet_count) > int(tweetIn.favorite_count)):
        api.update_status(f[num1 + lvl*2])
    elif int(tweetIn.retweet_count) < int(tweetIn.favorite_count):
        api.update_status(f[num2 + lvl*2])

if lvl == 2:
    if (int(tweetIn.retweet_count) > int(tweetIn.favorite_count)):
        api.update_status(f[num1 + lvl*2])
    elif int(tweetIn.retweet_count) < int(tweetIn.favorite_count):
        api.update_status(f[num2 + lvl*2])
