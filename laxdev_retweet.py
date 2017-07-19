#import required modules
from twython import Twython, TwythonError
import pprint #makes the data returned form twitters api more readable
import auth
pp = pprint.PrettyPrinter(indent=1)#set indentation level

#our keys to intereact with twitters api
consumer_key        = auth.consumer_key
consumer_secret     = auth.consumer_secret
access_token        = auth.access_token
access_token_secret = auth.access_token_secret

#filters
naughty_words = ["NFL", "angry", "sad", "kardashian", "likeforlike", "instalike", "hot", "growth_hacking"]
good_words = [ "#tech", "#code", "#computers", "#technology", "#programming", "#software", "#hardware", "#linux"] 
findlist = " OR ".join(good_words)
blacklist = " -".join(naughty_words)
keywords = findlist + blacklist

#passing the keys to to Twython
twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)

#retweet tweets of interest        
search_results = twitter.search(q=keywords, count=10, result_type='recent')
#pp.pprint(search_results)
try:
    for tweet in search_results["statuses"]:
       #if tweet["retweet_count"] > 50:
         #pp.pprint(tweet)
         try:
            twitter.retweet(id = tweet["id_str"])
            print("tweeted: " + tweet["id_str"])
         except TwythonError as e:
            print(e)
except TwythonError as e:
    print(e)
