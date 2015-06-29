import tweepy
import os
from datetime import datetime
from subprocess import call


class Tweet:

    def __init__(self, conf):
        auth = tweepy.OAuthHandler(conf["consumer_key"], conf["consumer_secret"])
        auth.set_access_token(conf["access_token"], conf["access_token_secret"])
        self.api = tweepy.API(auth)

        # camera settings
        #self.picture_width = '300'
        #self.picture_height = '300'
        #self.camera_time = '100'
        self.picture_name = "parking.jpg"
        self.picture_full_path = os.getcwd() + '/' + self.picture_name

    def send_tweet(self, img, message=''):
        # Tweet message
        date = datetime.now()
        date = date.strftime('Day: %Y-%m-%d   Time: %H:%M:%S')

        # Take photo of parking spot
        #command = 'raspistill -t ' + self.camera_time \
        #            + ' -w ' + self.picture_width \
        #            + ' -h ' + self.picture_height \
        #            + ' -o ' + self.picture_name \
        #            + ' -n'
        #call([command], shell=True)

        img.save(self.picture_full_path)

        # send tweet
        self.api.update_with_media(self.picture_full_path,  status=date + ': ' + message)

        # remove picture
        os.remove(self.picture_full_path)

