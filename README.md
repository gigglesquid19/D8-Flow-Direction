# D8-Flow-Direction

Contents
-------------------
- README
- License File
- Snowslope3.csv
- D8.py (contains the flow direction tool source code)
- D8framework.py (contains the functions)
- D8debug.py

Software Outline
--------------------
One of the keys to deriving hydrologic characteristics of a surface is the ability to determine the direction of flow from every cell in the raster. This is done with the Flow Direction tool.

Features
--------------------
- Select any raster elevation dataset in csv format and model the direction of water flow across the surface
- Generates x1 Digital Elevation Model graphical output for the elevation dataset 
- Generates x1 D8 Flow Direction Model graphical output for the elevation dataset
- Saves the Flow Direction data to a new csv file
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
Once run, the program will read the elevation raster dataset, in csv format. To change the csv file to another elevation raster dataset change the filename on line 24. The program, scans the height and width of the dataset saving the values, makes a deep copy of the dataset generates a digital elevation model which is displayed as a graphical output. The program then begins iterating through the values of (k) in each row (l). The program determines if the location of the pixel is a corner, a side or near the center and relays the elevation values of its neighbours in a pixellist. If the value is not present in the dataset its value is assumed to be the highest (255) so it is disregarded. The whichpix function determines the neighbor with the largest difference in elevation relaying this information into the flow direction function. This function then determines if the pixel in question is orthogonal or diagonal and calculates the directional code. This value is then updated in the original cell. Once the program reaches the final pixel (bottom right), it then generates a flow direction model which is displayed as a graphical output. Next, it saves the flow direction dataset to a new csv file then signals to the user that the model is complete along with a runtime.

Functions
--------------------
The program includes x3 functions which can be found in the D8framework.py script. The functions include: Whichpix, Flowdirection and Update.


Development Problems
---------------------


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
With the addition of more time spent on this model, the developers would have added in conditions to the model to strengthen the D8 Flow Direction tool. Conditions would include: if all neighbors are higher than the processing cell, it would be considered noise, be filled to the lowest value of its neighbors, and have a flow direction toward this cell, if a one-cell sink is next to the physical edge of the raster or has at least one NoData cell as a neighbor, it is not filled due to insufficient neighbor information, if two cells flow to each other, they are sinks and have an undefined flow direction.

License
---------------------
Creative Commons Zero v1.0 Universal

---------------------------------------------------------------------
Programming for Geographic Information Analyses - University of Leeds
