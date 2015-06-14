
from tweet import Tweet

twitter_configuration = {
    'consumer_key' : '......',
    'consumer_secret' :  '.....',
    'access_token' : '.....',
    'access_token_secret' : '........'
}

############################

tweet = Tweet(twitter_configuration)
tweet.send_tweet()