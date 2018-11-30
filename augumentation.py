import matplotlib.pyplot as plt
import numpy as np

#Image Transformations
from skimage import data
from skimage.transform import rescale
from skimage.util import random_noise
from skimage.color import rgb2gray
from skimage import util
from skimage.transform import rotate
from skimage import exposure
from scipy import ndimage

import warnings
import cv2
import os
warnings.filterwarnings("ignore")
from PIL import Image

path1 = "leaf_good"   
path2 = "leaf_good_aug"    

def image_augmentation(original_image,i,j):
    aug_list=[]

    image_rescaled = rescale(original_image, 1.0 / 4.0)
    cv2.imwrite(path2 +str(i)+str(j)+".jpg",image_rescaled)

    image_with_random_noise = random_noise(original_image)
    cv2.imwrite(path2 +str(i)+str(j)+".jpg",image_with_random_noise)

    gray_scale_image = rgb2gray(original_image)
    aug_list.append(gray_scale_image)

    color_inversion_image = util.invert(original_image)
    aug_list.append(color_inversion_image)

    image_with_rotation = rotate(original_image, 45)
    aug_list.append(image_with_rotation)

    v_min, v_max = np.percentile(original_image, (0.2, 99.8))
    better_contrast = exposure.rescale_intensity(original_image, in_range=(v_min, v_max))
    aug_list.append(better_contrast)

    #adjusted_gamma_image = exposure.adjust_gamma(original_image, gamma=0.4, gain=0.9)
    #aug_list.append(adjust_gamma)

    log_correction_image = exposure.adjust_log(original_image)
    aug_list.append(log_correction_image)

    sigmoid_correction_image = exposure.adjust_sigmoid(original_image)
    aug_list.append(sigmoid_correction_image)

    horizontal_flip = original_image[:, ::-1]
    aug_list.append(horizontal_flip)

    vertical_flip = original_image[::-1, :]
    aug_list.append(vertical_flip)

    blured_image = ndimage.uniform_filter(original_image, size=(11, 11, 1))
    aug_list.append(blured_image)

    return aug_list



listing = os.listdir(path1)    
for file in listing:
    img = cv2.imread(path1 +"/"+ file)
    cv2.imshow("img",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    
    lst=image_augmentation(img,1,1)
    j=0
    for image in lst:
        
        print("Writing image"+str(i)+str(j))
        j=j+1
    i=i+1           
    


