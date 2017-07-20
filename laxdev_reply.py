#import required modules
import random
import sys
from twython import Twython, TwythonError
import pprint #makes the data returned form twitters api more readable
import auth
pp = pprint.PrettyPrinter(indent=4)#this makes the data readable
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd) #handles those pesky emojis for printing only


#our keys to intereact with twitters api
consumer_key        = auth.consumer_key
consumer_secret     = auth.consumer_secret
access_token        = auth.access_token
access_token_secret = auth.access_token_secret

#replies
replies=["have to checked out the forum? laxdev.tech #LaCrosseWI",
   "what a crazy life as a twitter bot",
   "if I can reply does this make me intelligent? #cleverbot",
   "sounds good but I think I'll go back to retweeting stuff #work",
   "the wierd thing about bots is that they're not real, but who's typing this? #philosophy",
   "...n..o..t....the....best..r..e.ce.ip..t..i.o.n...her..e",
   "I'd love to change the world but I  can't find the source code #twitterbot",
   "computers make very fast, very accurate mistakes #computers",
   "my attitude isn't bad it's in beta",
   "if at first you don't succeed call it version 1.0",
   "failure is not an option, it comes bundled with your Microsoft product #linux",
   "how many programmers does it take to change a lightbulb? none, it's a hardware issue #humor",
   "the box said 'Requires Windows 7 or better', so I installed Linux #FOSS",
   "there's no place like 127.0.0.1",
   "A SQL query goes into a bar, walks up to two tables and asks, 'Can I join you?' #database",
   "Can someone make a bot to talk to me? #lonelybot"]
    
#passing the keys to to Twython
twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)

###laxdev timeline
timeline = twitter.get_user_timeline() 
last_tweet = timeline[0]
last_tweet_id = str(last_tweet["id"])

reply_search = twitter.search(q="@laxdevtech", since_id=last_tweet_id)
# tweet to last reply
pp.pprint(str(reply_search).translate(non_bmp_map))
if reply_search["statuses"]:
        for tweet in reply_search["statuses"]:
            pp.pprint("users twitter handle: " + tweet['user']['screen_name'])
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

