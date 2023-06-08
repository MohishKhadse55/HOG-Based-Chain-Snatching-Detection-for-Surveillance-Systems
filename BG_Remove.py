from rembg import remove
import cv2
import glob
import os


image_path = glob.glob(r'path of dataset folder path\*.jpg')

i = 0
for image in image_path:
    input = cv2.imread(image)
    input  = cv2.resize(input, (256, 256))
    output = remove(input)

      # Save the output image in the 'Abnormal' folder with a filename of 'imageXX.jpg'
    cv2.imwrite(r'Removed Background Folder path\image%02i.jpg' % i, output)
    i += 1
