from SimpleCV import *


roi = {
    'x' : 100,
    'y' : 0,
    'width' : 200,
    'height' : 100,
    'area' : 20000
}

CAMERA = {
    'width' : 640,
    'height' : 480
}

cam = Camera(1, {'width': 640, 'height': 480})

class AlgorithmX:

    # avg amount of white pixels in ROI
    percent_of_white_px = 0

    # initialize avg
    def __init__(self, camera, roi):
        for i in range(60):
            img = cam.getImage()
            img = img.crop(roi['x'], roi['y'], roi['width'], roi['height'])
            img = img.edges()
            img = img.getNumpy().flatten()
            self.percent_of_white_px =  self.percent_of_white_px + (cv2.countNonZero(img) / roi['area'])
            print (self.percent_of_white_px )
        print ('Total avg: ' + str(self.percent_of_white_px))

    def perform_A(self, img):
        img = img.getNumpy().flatten()
        white_px = cv2.countNonZero(img) / roi['area']

        subt = abs(self.percent_of_white_px - white_px)

        if subt > 3:
            # stop thread for 2 sec and calculate once again
            print ("...")

            self.percent_of_white_px = "nowa wartosc"
        else:
            self.percent_of_white_px = (self.percent_of_white_px + white_px) / 2.0










