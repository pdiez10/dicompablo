# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 13:59:42 2021

@author: pablo
"""

#Import the libraries needed
import pydicom
from scipy.ndimage import gaussian_filter as gaussflt
from scipy.ndimage import rotate
import glob
import os 
import cv2
import sys

#Create the filter function 
class DcmFilter:
 
    
    
    def __init__(self, path, sigma=3):
        
        
        #Read the image
        image_dcm = pydicom.dcmread(path)
        
        #Convert the image into a numpy array
        self.original = image_dcm.pixel_array
        
        #Filter the image using sigma
        self.filtered =  gaussflt(self.original,sigma)
        
        #Extract the image position of the patient from the dicom file
        self.ipp = image_dcm['ImagePositionPatient'][:]
        
        
class DcmRotate:
    
    def __init__(self, path, angle=180):
       
        #Read the image
        image_dcm = pydicom.dcmread(path)

        #Convert the image into a numpy array
        self.original = image_dcm.pixel_array
        
        #Only if its 90 multiple
        if 90 % angle ==0:
        #Rotate the image 
            self.img_rotate = rotate(self.original,angle)
            
        #Extract the image position of the patient from the dicom file
        self.ipp = image_dcm['ImagePositionPatient'][:]
        
        

def check_ipp(dcm_rotate,dcm_filtered):
    
    #Extract the first list of IPPs values
    ipp1 = dcm_rotate.ipp
    
    #Extrac the secont list of IPP values
    ipp2 = dcm_filtered.ipp
    
    veredict = ipp1==ipp2
    
    return veredict


def main(input_folder):
    
    
    
    paths = glob.glob(input_folder +'\*.dcm')
    
    print(paths)
    
    number_img = len(paths)
    
    if number_img!=2:
        
        raise IncorrectNumberOfImages
        

    
    img1_flt = DcmFilter(paths[0], sigma = 3)
    
    img2_flt = DcmFilter(paths[1], sigma = 3)
    
    
    
    if check_ipp(img1_flt, img2_flt):
        
        raise SameImagePositionPatient
        
    
    


    res_original = img1_flt.original - img2_flt.original
    
    res_flt = img1_flt.filtered - img2_flt.filtered
    

    root = os.path.join(input_folder + '/residues')

    root = root.replace( '\\'  , '/')
    
    if os.path.exists(root)==False:  
    
        os.mkdir(root)
    
        
    
    cv2.imwrite(root + '/unfiltered_residue_original.jpg',res_original)
    
    cv2.imwrite(root + '/unfiltered_residue_flt.jpg',res_flt)
    




class IncorrectNumberOfImages(Exception):


    def __init__(self,  message='Incorrect number of images, Aborting'):
        
        self.message = message
        
        super().__init__(self.message)
        

class SameImagePositionPatient(Exception):


    def __init__(self,  message='The DICOM files appear to be the same'):
        
        self.message = message
        
        super().__init__(self.message)


if __name__ == '__main__':
    main(sys.argv[1])