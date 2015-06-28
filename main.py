from SimpleCV import *
import sys

if len(sys.argv) < 4:
    print "Usage: main.py x y width height"
    sys.exit(1)

cam = Camera(1, {'width': 640, 'height': 480})

roi = {'x': sys.argv[1], 'y': sys.argv[2], 'w': sys.argv[3], 'h': sys.argv[4]}

# globals
n = 20
buffer = []
avg = 0
threshold = 3;

def count_white_pixels():
    img = cam.getImage()
    img = img.crop(roi['x'], roi['y'], roi['w'], roi['h'])
    img = img.edges(50, 200)
    imgmat = img.getNumpy().flatten()
    whitepx = cv2.countNonZero(imgmat) / (int(roi['w']) *  int(roi['h']))
    return whitepx

# prepare buffer
for i in range(n):
    buffer.append(count_white_pixels())

avg = sum(buffer)/n

while True:
    whitepx = count_white_pixels()
    current_diff = avg - whitepx

    # check parking spot
    if abd(current_diff) > threshold:
        if current_diff > 0 :
            print 'Przyjechalo +++'
        else:
            print "Odjechalo ---"

    # update buffor
    remove_element = buffer.pop(0)
    buffer.append(whitepx)
    avg += whitepx/n - remove_element/n






