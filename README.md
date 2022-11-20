# Image-Filters

This program contains one file - main.py.

#HOW TO RUN#
-Open command prompt and type 'pip install pykuwahara'
-Make sure you have TKinter, PIL, numpy, and OpenCV installed as well
-Open 'main.py'

#HOW TO USE#
-Click the 'Select an image' button
-Browse directory for image you want to use
-Click the file you want, then click 'Open'
-The image on the left is the image you want to filter; the image on the right is the image after the
filter/noise has been applied
-To apply the 5x5 Kuwahara filter, click the '5x5 Kuwahara' button
-To apply the 5x5 Median filter, click the '5x5 Median' button
-To apply the 5x5 Gaussian filter, click the '5x5 Gaussian' button
	>Notice the textbox under 'Sigma for Gaussian Filter' label. To set a specific sigma value,
	type a number into the textbox; the program will automatically detect the number in the box
	without any need to hit Enter or click any button
	>If textbox is empty, the gaussian filter will use the default sigma value of 1
-To apply the 5x5 Triangle filter, click the '5x5 Triangle' button
-To add noise to the image you want to filter, click the 'Add Noise' button
-If you want to use the result image on the right for further filtering, click the 'Update Source'
button; this will swap the images around
-If you want to save the result image on the right, click the 'Save Image' button - this will create
an .jpg image file of the image on the right in the same folder the program is located in as 
'SavedImage.jpg'
-If you want to filter another image, click the 'Select an image' button to browse and open another 
image
-To close the program, click the 'X' button on the top-right

#BUGS#
-None found
