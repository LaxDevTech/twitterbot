import sys
import time
import pprint
import random
from twython import Twython, TwythonError
import auth

pp = pprint.PrettyPrinter(depth=4)  # this makes the data readable

# handles those pesky emojis for printing only
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)


# functions start
def greeter(real_name, username, location=None):
    if location is None:
        location = "twitterverse"
    # greeter
    greeter_list = ["hello " + name + " whats the weather like in " + location,
                    "thanks for following, " + name + "I'm a semi smart twitterbot floating somewhere near " + location,
                    name + "," + "are you a bot aswell? What's a " + location,
                    "hey " + name + ", tweet me anytime #chatty",
                    "what are followers? and whats a " + name + "? #twitterbot"]
    number = random.randrange(0, len(greeter_list))
    twitter.update_status(status="@" + username + " " + greeter_list[number] + " ")
    print("tweeted: " + "@" + username + " " + greeter_list[number] + " ")


def reply():
    # replies
    replies = ["have to checked out the forum? laxdev.tech #LaCrosseWI",
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
    # laxdev timeline
    timeline = twitter.get_user_timeline()
    last_tweet = timeline[0]
    pp.pprint(str(last_tweet).translate(non_bmp_map))
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


def retweet():
    # retweet tweets of interest
    search_results = twitter.search(q=keywords, count=20, result_type='popular')
    # pp.pprint(str(search_results["statuses"]).translate(non_bmp_map))
    try:
        for tweet in search_results["statuses"]:
            if tweet["retweet_count"] > 50:
                # pp.pprint(tweet)
                try:
                    twitter.retweet(id=tweet["id_str"])
                    # print("tweeted" + tweet)
                except TwythonError as e:
                    print(e)
    except TwythonError as e:
        print(e)
    print("nothing to retweet....")


# functions end

# our keys to intereact with twitters api
consumer_key = auth.consumer_key
consumer_secret = auth.consumer_secret
access_token = auth.access_token
access_token_secret = auth.access_token_secret

# filters
naughty_words = ["NFL", "angry", "sad", "kardashian", "likeforlike", "instalike", "hot", "growth_hacking", "#free",
                 "#eBay"]
good_words = ["#tech", "#code", "#computers", "#technology", "#programming", "#software", "#hardware", "#linux"]
findlist = " OR ".join(good_words)
blacklist = " -".join(naughty_words)
keywords = findlist + blacklist

# passing the keys to to Twython
twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)

while True:
    reply()
    retweet()
    followers = twitter.get_followers_ids(screen_name="laxdevtech")  # list followers of laxdevtech
    try:
        try:
            prev_last_follower  # checks for undefined
        except:
            prev_last_follower = None  # this gives a value to prev_last_follower
        # print(followers['ids'][0])
        last_follower = followers['ids'][0]  # latest_follwoer
        if prev_last_follower == last_follower:
            print("no new followers, latest: " + username)
            lookup = twitter.lookup_user(user_id=last_follower)
            # pp.pprint(str(lookup).translate(non_bmp_map))
            username = lookup[0]["screen_name"]
        else:
            lookup = twitter.lookup_user(user_id=last_follower)
            # pp.pprint(str(lookup).translate(non_bmp_map))
            username = lookup[0]["screen_name"]
            name = lookup[0]["name"]
            print("new follower: " + username)
            # lookup[0]["location"]
            location = lookup[0]["location"]
            # print(location)
            greeter(name, username, location)
        prev_last_follower = last_follower

        # print(prev_last_follower)
        print("complete list of follower ids:")
        for follower in followers['ids']:
            print(follower)

        ## TODO do they want the bot
        ##twitter.create_friendship(user_id=followers_ids)
    except TwythonError as e:
        print(e)
    time.sleep(120)
