import os
import cv2
import numpy as np

def get_preprocessed_images(img_dir_path, img_list):
  
  '''
  Function to read and preprocess the images

  parameters:
    img_dir_path : path of directory where images are stores
    img_list : list of length n, for n images, containing image names

  return :
    np.array(images_list) : a numpy array containing pre-processed images; dimension --> (number of images, height, width, channels)
  
  '''

  images_list = []
  for img in img_list:

    img = os.path.join(img_dir_path, img)
    image = cv2.imread(img)
    image = image.astype("float32") / 255.0
    image = cv2.resize(image,(256,256))

    images_list.append(image)

  return np.array(images_list)