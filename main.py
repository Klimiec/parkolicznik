from SimpleCV import *
import sys
import time

if len(sys.argv) < 4:
    print "Usage: main.py x y width height"
    sys.exit(1)

cam = Camera(1, {'width': 640, 'height': 480})

roi = {'x': sys.argv[1], 'y': sys.argv[2], 'w': sys.argv[3], 'h': sys.argv[4]}

# globals
n = 20
buffer = []
avg = 0
threshold = 3
current_diff = 0

def count_white_pixels():
    img = cam.getImage()
    img = img.crop(roi['x'], roi['y'], roi['w'], roi['h'])
    img = img.edges(50, 200)
    imgmat = img.getNumpy().flatten()
    whitepx = (cv2.countNonZero(imgmat) * 100) / (int(roi['w']) * int(roi['h']))
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
                print 'Przyjechalo +++'
            else:
                print "Odjechalo ---"

    # update buffer
    remove_element = buffer.pop(0)
    buffer.append(whitepx)
    avg = sum(buffer)/n







