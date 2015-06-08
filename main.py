from SimpleCV import *
import sys

if len(sys.argv) < 4:
    print "Usage: main.py x y width height"
    sys.exit(1)

cam = Camera(1, {'width': 640, 'height': 480})

roi = {'x': sys.argv[1], 'y': sys.argv[2], 'w': sys.argv[3], 'h': sys.argv[4]}

while True:
    img = cam.getImage()
    img = img.crop(roi['x'], roi['y'], roi['w'], roi['h'])
    img = img.edges(50, 200)
    imgmat = img.getNumpy().flatten()
    whitepx = cv2.countNonZero(imgmat) / 3072.0
    print whitepx
    img.show()

