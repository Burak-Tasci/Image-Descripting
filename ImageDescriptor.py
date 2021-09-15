import numpy as np
import pandas as pd
import cv2
import imutils

class ImageDescriptor:
    def __init__(self,bins):
        self.bins = bins
    def describe(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        features = []
        (h, w) = image.shape[:2]
        (top_cX, top_cY) = (int(w * 0.25), int(h * 0.30))
        (bottom_cX, bottom_cY) = (int(w * 0.75), int(h * 0.60))
        centerX = int(w / 2)
        centerY = int(h / 2)

        bottom_coordinates = (centerX, bottom_cY)
        black = np.zeros((h,w), dtype = np.uint8)
        bottom_ellipse_mask = cv2.ellipse(black, bottom_coordinates, (100, 100), 0,
                          0, 360, (255, 255, 255), -1)
        top_coordinates = (centerX, top_cY)
        black = np.zeros((h,w), dtype = np.uint8)
        top_ellipse_mask = cv2.ellipse(black, top_coordinates, (100, 100), 0,
                          0, 360, (255, 255, 255), -1)
        
        ### First masked image with ellipse areas
        top_and_bottom_mask = cv2.add(top_ellipse_mask, bottom_ellipse_mask)
        ellipse_masked_image = cv2.bitwise_and(image,image,mask = top_and_bottom_mask)

        left_top_corner = (centerX - 100,top_cY - 100)
        right_bottom_corner = (centerX + 100, bottom_cY + 100)
        black = np.zeros((h,w), dtype = np.uint8)
        rect_mask = cv2.rectangle(black,left_top_corner,
                         right_bottom_corner,
                          (255,255,255), -1)

        substracted_rect_and_ellipse_mask = cv2.subtract(rect_mask,top_and_bottom_mask)
        ### Second masked image without ellipse areas
        substracted_rect_and_ellipse_mask_image = cv2.bitwise_and(image,image,mask = substracted_rect_and_ellipse_mask)
        hist = self.histogram(image, top_and_bottom_mask)
        features.extend(hist)
        return features

    def histogram(self, image, mask):
		# extract a 3D color histogram from the masked region of the
		# image, using the supplied number of bins per channel
        hist = cv2.calcHist([image], [0, 1, 2], mask, self.bins,
			[0, 180, 0, 256, 0, 256])
		# normalize the histogram if we are using OpenCV 2.4
        if imutils.is_cv2():
	        hist = cv2.normalize(hist).flatten()
		# otherwise handle for OpenCV 3+
        else:
	        hist = cv2.normalize(hist, hist).flatten()
		# return the histogram
        return hist
        

