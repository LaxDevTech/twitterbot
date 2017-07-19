from twython import Twython, TwythonError
import auth


#our keys to intereact with twitters api
consumer_key        = auth.consumer_key
consumer_secret     = auth.consumer_secret
access_token        = auth.access_token
access_token_secret = auth.access_token_secret

# passing the keys to to Twython
twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)

message = "Hello world"

twitter.update_status(status=message)
print("The bot tweeted: %s" % message)
