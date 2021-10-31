# dicompablo

Along this code several classes and functions were implemented

1. Filter image class DcmFilter:

In this class the dicom image is readed with the help of pydicom library giving the path and the sigma value for the gaussian filter
After this we transform the dcm image to numpy array and filter the numpy image
Finally the IPP values are obtained from th dcm image file and stored in a list 

2. Rotation image class DcmRotate:

The schedule is very similar from last one, giving as input the path of the image and rotation degrees
In this case the angle of rotation should by multiple of 90º
We also store the IPP values, the original image and the rotated one

3. check_ipp function:

This function aims to compare the IPP values extracted giving as output a boolean (True False)

4. Residue image obtainment mainfunction:

The residue of the filtered and unfiltered images should be calculated but only if the IPP values are different and the number of dcm  images on the selected path are 2. 
If these criterias are not fullfilled several Exceptions appeared (also implemented for this task ) 
To do so the IPP values are compared using the previously implemented check_ipp function 
The residue images in JPG format are stored in a residue folder created for this task (if there is no residue folder it should be created automatically).


All this module is able to be imported (previousle saved in the corresponding path)
and we also can execute it as a script using the command: !python -m dicomhandling input_folder 
