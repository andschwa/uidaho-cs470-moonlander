Moonlander Project
==================
Artificial Intelligence 
-----------------------
* CS470/570 
* Spring 2013
* Project #3a
* Due: Wednesday, April 3rd 

Project: Create and train an Artificial Neural Network (ANN) to control and safely land a moonlander on a variety of different 'planents' with acceleration due to gravity varying from 1 to 3 in increments of 0.1.

The basic moonlander code (written in C++) is available here. This code was written for a Windows platform, using the Dev-C++ compiler and OpenGL. However, you may use the language and platform of your choice. The code for the 'physics' of the moonlander is relatively simple and should be easy to port to the language/platform of your choice. Graphical output is not required.

The moonlander is controlled by setting the 'burn' and 'thrust'. Burn controls vertical movement and thrust controls the horizontal movement. Both values are set in the control() function within the lander class. Your goal is to fill in the conrol() function with an ANN that safely lands the moonlander.

Requirements:
-------------
The ANN should have 7 inputs:
* height
* xPosition
* Yvelocity
* Xvelocity
* wind
* acceleration
* fuel 

The ANN should have two outputs:
* burn
* thrust

The outputs can be scaled. Otherwise the structure of the NN, hidden layers, recurent connections, etc. is your choice.

Algorithms:
-----------
The program must use an ANN. You may train the weights of the ANN or try to set the weights of the ANN by hand - but see scoring below. During training make sure the lander is trying to land under a variety of accelerations.

Scoring:
--------
The project will be scored out of 100. 15 of those points are for the training method - if any. I.e. if you only set the weights by hand the max score is 85/100.

Testing:
--------
Once the ANN is trained, either via an algorithm or by hand, run the program at least 10 times each for accelerations from 1 to 3. Keep track of how many times it lands successfully for each rate of acceleration.

Hand-In:
--------
* You need to hand in typed write-up containing the following:
* An abstract summarizing what you did and what the results were.
* An algorithm section explaining your program. Including,
* A description of the ANN: # of nodes, node types, scaling, etc.
* A dscription of the training algorithm - if any
* A results section. Including,
* A presentation of the 'average' results. E.g. what was the success rate of the control ANN.
* A discussion of how the program behaved. Did it have any strengths or weaknesses?
* A conclusion section.
