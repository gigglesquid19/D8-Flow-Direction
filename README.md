# D8-Flow-Direction

Contents
-------------------
- README
- License File
- Development Doc
- Snowslope3.csv (raw data)
- D8.py (contains the flow direction tool source code)
- D8framework.py (contains the functions)
- D8debug.py
- D8framedebug.py

Software Outline
--------------------
One of the keys to deriving hydrologic characteristics of a surface is the ability to determine the direction of water flow from every cell in the raster, this is done with a Flow Direction tool.

Features
--------------------
- Select any raster elevation dataset in csv format and model the direction of water flow across the surface
- Generates x1 Digital Elevation Model graphical output for the elevation dataset 
- Generates x1 D8 Flow Direction Model graphical output for the elevation dataset
- Saves the Flow Direction dataset to a new csv file
- Includes debugging versions of the model scripts with print statements left present

How to use?
-------------------
1) Download and open D8.py within a python IDE
2) Download and open D8framework.py within a python IDE
3) Within D8.py ensure associated script (agent framework) is imported:
4) Ensure both scripts are within the same working directory
5) Run >

What to expect?
---------------------
Once run, the program will read the elevation raster dataset, in csv format. To change the input csv dataset to another file, change the filename on line 24. The program, scans the height and width of the dataset and saves the values. It then makes a deep copy of the dataset and generates a digital elevation model from it which is displayed as a graphical output. The program then begins iterating through the values of (k) in each row (l) top to bottom (inner loops) and from left to right (outer loops). The program determines if the location of the pixel is a corner, a side or near the center and can form a 3 x 3 grid and relays the appropriate elevation values of its neighbours in a pixellist. If the value is not present in the dataset its value is assumed to be the highest (255) so it is disregarded. The whichpix function determines the neighbor with the largest difference in elevation relaying this information into the flow direction function. This function then determines if the pixel in question is orthogonal or diagonal and uses a formula to calculate the directional code. This value is then updated by a function in the original cell. Once the program reaches the final pixel (bottom right), it then generates a flow direction model which is displayed as a graphical output. Lastly, it saves the flow direction dataset to a new csv file then signals to the user that the model is complete along with a runtime.

Functions
--------------------
The program includes x3 functions which can be found in the D8framework.py script. The functions include: Whichpix, Flowdirection and Update.
Whichpix -        Takes in the values of l and k and elev_copy dataset, along with list of neighboring pixels with values. Loops through the pixellist and finds the and                         calculates a droplist of the differences between neighboring pixel elevations and original pixel elevation. Next, finds the lowest drop value, the 
                  elevdeduct and notes the pixelid, returning both.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Flow Direction -  Takes in the value of l and k and the elev_copy dataset, along with th elededuct, pixid returned from whichpix function and the diagonal boolean and                           pixellist. Depending on the pixelid and boolean, the function calc whether pixel is orthogonal or diagonal from original pixel and uses formula to calculate                   the max_drop, updating the pixel. It also returns the flow direction value.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Update -          This simple function updates the pixel value with the directional code returned from the flow direction function

Development Problems
---------------------
For more information please see the development document

Known Issues
---------------------
There are no known issues with this program.

Support
---------------------
If you are having issues, please let us know
The creator can be reached by emailing: ----------@gmail.com

Testing
---------------------
A timing function was added to the Stopping Condition so that each time the model finishes, the user is informed in the console how long it ran for. There is a debug version of the D8.py and D8framework.py scripts which have the print statements from development left inside.

Ideas for Further Development
-----------------------------
With the addition of more time spent on this model, the developers would have alterred the graphical output of the D8 Flow Direction Tool from a filled contour to a streamflow. In addition, some extra conditions would have been added such as: if all neighbors are higher than the processing cell, it would have been considered noise and be filled to the lowest value of its neighbors and have a flow direction towards this cell or if two cells flow to each other, they are sinks and would be assigned an undefined flow direction.

License
---------------------
Creative Commons Zero v1.0 Universal

---------------------------------------------------------------------
Programming for Geographic Information Analyses - University of Leeds
