# Robotic-Hand Overview

## Construction
This is the code for my senior project, building a rock, paper, scissors-playing hand. The open-source design for the 3d-printed arm comes from the [InMoov Robot](http://inmoov.fr). The fingers are actuated by 5 servos that are controlled by an arduino, powered by two 9-volt batteries in parallel. The arduino receives commands from my computer via serial port. 

## Code
The Arduino code simply receives key presses from the laptop and sends the corresponding command to the servos to move the fingers.

The main driver program is written in Python and image processing is performed using the openCV library. The image processing steps are as follows:
1. Take image and make grayscale
2. Apply threshold to all pixels (if brighter than a certain value, make black; else make white)
3. Take hull of largest white area (presumably the hand)
4. Look for indentations (these should be the gaps between the fingers)
5. Only count the number of indentations with angle < 90 degrees


You can find my final presentation of the arm [here](https://youtu.be/f7hHvrXVjak) and the slides [here](https://docs.google.com/presentation/d/1qPzilUTlk5lW5QpsaAyi3jth-C149x8M6q1rPRpe0uw)

