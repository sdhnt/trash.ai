import os
import glob
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2

# defining global variable path
image_path = "recycled_set/train_unproc/plastic"

def loadImages(path):
    # Put files into lists and return them as one list of size 4
    image_files = sorted([os.path.join(path, file) for file in os.listdir(path) if file.endswith('.jpg')])
    return image_files



# Preprocessing
def processing(data):
    # loading image
    # Getting 3 images to work with 
    #img = [cv2.imread(i, cv2.IMREAD_UNCHANGED) for i in data[:3]]

    img = [cv2.imread(i, cv2.IMREAD_UNCHANGED) for i in data[:]]
    #print(img)
    # --------------------------------
    # setting dim of the resize
    height = 250
    width = 250
    dim = (width, height)
    res_img = []
    for i in range(len(img)):
        res = cv2.resize(img[i], dim, interpolation=cv2.INTER_LINEAR)
        res_img.append(res)

    # Remove noise
    # Gaussian
    no_noise = []
    for i in range(len(res_img)):
        blur = cv2.GaussianBlur(res_img[i], (5, 5), 0)
        no_noise.append(blur)

    return no_noise





def main():
    # calling global variable
    global image_path
    '''The var Dataset is a list with all images in the folder '''          
    dataset = loadImages(image_path)
     
    print("List of files the first 3 in the folder:\n",dataset[:3])
    print("--------------------------------")
    
    # sending all the images to pre-processing
    pro = processing(dataset)

    counter=0
    for i in pro:
        counter=counter+1
        cv2.imwrite(image_path+'plastic' +str(counter)+'.jpg', i)

    


main()