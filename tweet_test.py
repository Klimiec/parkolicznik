
from tweet import Tweet

twitter_configuration = {
    'consumer_key' : '9yHE3TdYv9cVbVi5tme6C76Gj',
    'consumer_secret' :  'noaO55Ra6jxWHYX4HDAo24PRskms7L8ZWMerNEAEeNCdOlbmvI',
    'access_token' : '383755446-jhC6SSZ0NoeEz9FSiiQ4SKB1SAZ3KtFUJ3Vzxpbl',
    'access_token_secret' : 'yfYvmFgfTCCWiJKug9zM2Yde169XUx75Jyt9sxywTGxQj'
}

############################

tweet = Tweet(twitter_configuration)
tweet.send_tweet()