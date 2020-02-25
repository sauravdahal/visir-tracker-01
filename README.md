# Practical Assignment 1
Please put your name (or names if you work in a group) here:  
**Name**: Saurav Dahal
## Problem 1.1
### Calculate Frames-per-Second (FPS) (Points 30)
1. Fork the current repository
2. Study the new framework-code of 
    - main.cpp
3. Check that the code is running correctly: it should show the video stream from the web-camera of your laptop.
4. Calculate average fps and print it to console every 2 seconds. Compare Debug and Release versions.
### Note
MacOS users may need to launch the application with administrator right, to grant access to the web-camera.

## Problem 1.2
### Face detection (Points 70)
1. Read the OpenCV documentation about Viola-Jones face detector: [Cascade Classifier](https://docs.opencv.org/4.2.0/db/d28/tutorial_cascade_classifier.html)  
2. Implement face detection for the video strem from the web-camera using the ```cv::CascadeClassifier``` class.
3. Measure the FPS one more time. How FPS changed after incorporating the face detection into the framework?
### Note
Please do not copy-paste the example code from the OpenCV documentation, but try to understand the example code and implement the solution to the problem by yourself.


#Procedure:
```
sudo pip3 install numpy
```
```
pip3 install opencv-python
```

```
python3 problem1.py
python3 problem2.py
```


#Assignment 1
From my computer, the normal average fps computed was around 17.

#Assignment 2
The Cascade classifier fps was also around 17 so the implementation of cascade classifier didn't change time complexity. 
That means, cascade classifier is very effective.


