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

###laxdev timeline
timeline = twitter.get_user_timeline() 
last_tweet = timeline[0]
last_tweet_id = str(last_tweet["id"])

reply_search = twitter.search(q="@laxdevtech", since_id=last_tweet_id)
# tweet to last reply
if reply_search["statuses"]:
        for tweet in reply_search["statuses"]:
            pp.pprint(tweet['user']['screen_name'])
            user = tweet['user']['screen_name']
            text = tweet['text']
            name = tweet['user']['name']
            id = str(tweet['id'])
        header = "@" + user + " "
        reply = text.lower()
        number = random.randrange(0, len(replies))
        twitter.update_status(status=header + name + ", " + replies[number], in_reply_to_status_id=id)
        print("tweeted: " + header + name + ", " + replies[number])
else:
    print("no interaction")

