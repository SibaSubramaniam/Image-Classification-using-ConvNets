import cv2
import numpy as np
image = cv2.imread('leaf.JPG')

b = image.copy()
# set green and red channels to 0
b[:, :, 1] = 0
b[:, :, 2] = 0


g = image.copy()
# set blue and red channels to 0
g[:, :, 0] = 0
g[:, :, 2] = 0

r = image.copy()
# set blue and green channels to 0
r[:, :, 0] = 0
r[:, :, 1] = 0

b_mean=np.mean(b)
r_mean=np.mean(r)
g_mean=np.mean(g)

#Regularization
correct=2*b_mean/(b_mean+r_mean+g_mean)
wrong1= (r_mean-b_mean)/(r_mean+b_mean)
wrong2=(r_mean-b_mean)/g_mean
wrong3=(r_mean-b_mean)/(r_mean+b_mean+g_mean)


protein=correct*6.25



print(protein)
print(wrong1,wrong2,wrong3)