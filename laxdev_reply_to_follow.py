import sys
import time
import pprint
import random
from twython import Twython, TwythonError
import auth
pp = pprint.PrettyPrinter(depth=4)#this makes the data readable

#handles those pesky emojis for printing only
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

# functions start 
def greeter( real_name, username, location=None ):
    if location is None:
        location = "twitterverse"
    #greeter
    greeter_list = ["hello " + name + " whats the weather like in " + location,
                    "thanks for following, " + name + "I'm a semi smart twitterbot floating somewhere near" + location,
                    name + "," + "are you a bot aswell? What's a " + location,
                    "hey " + name + ", tweet me anytime #chatty",
                    "what are followers? and whats a " + name + "? #twitterbot"]
    number = random.randrange(0, len(greeter_list))
    twitter.update_status(status="@" + username  + " " + greeter_list[number] + " ")
    print("tweeted: " + "@" + username  + " " + greeter_list[number] + " ")
#functions end

#our keys to intereact with twitters api
consumer_key        = auth.consumer_key
consumer_secret     = auth.consumer_secret
access_token        = auth.access_token
access_token_secret = auth.access_token_secret

# passing the keys to to Twython
twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)


followers = twitter.get_followers_ids(screen_name = "laxdevtech") #list followers of laxdevtech
try:
    try: prev_last_follower # checks for undefined
    except:
        prev_last_follower = None # this gives a value to prev_last_follower
    last_follower  = followers['ids'][0]
    #print("the last follower: " + followers['ids'][0])    
    if prev_last_follower == last_follower:
        print("no new followers, latest: " + username)
        lookup = twitter.lookup_user(user_id=last_follower)
        #pp.pprint(str(lookup).translate(non_bmp_map))
        username = lookup[0]["screen_name"]        
    else:
        lookup = twitter.lookup_user(user_id=last_follower)
        #pp.pprint(str(lookup).translate(non_bmp_map))
        username = lookup[0]["screen_name"]
        name = lookup[0]["name"]
        print("new follower: " + username)
        #lookup[0]["location"]
        location = lookup[0]["location"]
        #print(location)
        greeter( name, username, location )
    prev_last_follower = last_follower
    
    #print(prev_last_follower)
    print("complete list of followers:")
    for follower in followers['ids']:
      print(follower)
    ## TODO
##api.create_friendship(user_id=followers_ids)
except TwythonError as e:
    print(e)
