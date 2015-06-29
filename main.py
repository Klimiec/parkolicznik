# coding=utf-8

from SimpleCV import *
import sys
import time
from tweet import Tweet

if len(sys.argv) < 4:
    print "Usage: main.py x y width height"
    sys.exit(1)

cam = Camera(1, {'width': 640, 'height': 480})

roi = {'x': sys.argv[1], 'y': sys.argv[2], 'w': sys.argv[3], 'h': sys.argv[4]}

twitter_configuration = {
    'consumer_key' : '9yHE3TdYv9cVbVi5tme6C76Gj',
    'consumer_secret' :  'noaO55Ra6jxWHYX4HDAo24PRskms7L8ZWMerNEAEeNCdOlbmvI',
    'access_token' : '383755446-jhC6SSZ0NoeEz9FSiiQ4SKB1SAZ3KtFUJ3Vzxpbl',
    'access_token_secret' : 'yfYvmFgfTCCWiJKug9zM2Yde169XUx75Jyt9sxywTGxQj'
}

tweet = Tweet(twitter_configuration)

# globals
n = 60
buffer = []
avg = 0
threshold = 3
current_diff = 0
img = None

def count_white_pixels():
    global img
    img = cam.getImage()
    img = img.crop(roi['x'], roi['y'], roi['w'], roi['h'])
    img_edge = img.edges(50, 200)
    img_mat = img_edge.getNumpy().flatten()
    whitepx = (cv2.countNonZero(img_mat) * 100) / (int(roi['w']) * int(roi['h']))
    return whitepx

# prepare buffer
print 'Filling buffer...'
for i in range(n):
    current_value = count_white_pixels()
    buffer.append(current_value)
    print 'Amount of elements in buffer: ' + str(len(buffer)) + ' | Current value: ' + str(current_value)

avg = sum(buffer)/n
print 'avg = ' + str(avg)

while True:
    whitepx = count_white_pixels()
    current_diff = avg - whitepx
    print 'Current: ' + str(whitepx) + "| avg: " + str(avg) + " | Diff: " +  str(current_diff)

    # check parking spot
    if abs(current_diff) > threshold:
        print 'Waiting 5 sec...'
        time.sleep(5)
        whitepx = count_white_pixels()
        current_diff = avg - whitepx
        if abs(current_diff) > threshold:
            if current_diff > 0 :
                print 'Vehicle arrived +++'
                tweet.send_tweet(img, 'Przyjechała niezła bryka!')
            else:
                print "Vehicle left ---"
                tweet.send_tweet(img, 'Odjechała w siną dal!')

    # update buffer
    remove_element = buffer.pop(0)
    buffer.append(whitepx)
    avg = sum(buffer)/n
