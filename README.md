# Document_scanner
This is a repository that is aimed to help you work around on a computer vision project which is a document scanner using OpenCV.

## The codebase

### requirements.txt
1.  Opencv - python
2.  numpy
3.  imutils

### Scanner.py
This python file takes the input from the user in the form of the image to be scanned and provides the scanned binary image as the output.
Necessary comments have been added for simplification of the code, but for further reference https://docs.opencv.org/4.x/index.html is a very good place to visit.

Words of Caution: To get a clean and market worthy scan please use a contrast background from the image. This helps in creating the edges of the document properly which is the backbone of this algorithm.

### Scanner_save_imgs.py
This is a python file to save outputs at various stages through the algorithm. You can additionally add cv.imwrite command anywhere to save the output.

## Additional Inputs
This folder is a collection of a few different images which can be used to test out the algorithm. It covers a wide range of possible images.

## Pitfalls
This directory contains a few challenges and problems one might face while implementing the algorithm.

## Outputs of various functions
It contains number of images of the outputs at various steps (like, grayscale, canny edge detection, perspective transformation, etc.) through-out the algorithm. The outputs are for the "input.jpg" image which can be found in the same directory.
