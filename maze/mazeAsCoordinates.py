
import cv2
import numpy as np
from pathlib import Path

# make image bnw
# pass through canny edge detector
path = '/home/ben/Desktop/laserHTN/maze/maze.png'
image = cv2.imread(path)
medianPixelVal = np.median(image)
sigma = 0.33
lower = int(max(0, (1.0 - sigma) * medianPixelVal))
upper = int(min(255, (1.0 + sigma) * medianPixelVal))
image = cv2.Canny(image, lower, upper)
cv2.imwrite('canny_maze.png', image)
