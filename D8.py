# -*- coding: utf-8 -*-
"""
Created on Fri May  7 10:46:58 2021

@author: Ciaran
"""
# Import Modules
import D8framework4
import matplotlib.pyplot as pyplot
import math
import csv
import copy
import sys
import time

# Global Variables
elev = []
elev_copy = []
k = 0
l = 0


# Opens csv file into reader, appends values to rowlist, rowlists to elevation
with open('snowslope3.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    tic = time.perf_counter()
    for row in csv_reader:
        rowlist = []
        elev.append(rowlist)
        for values in row:
            i = int(values)
            rowlist.append(i)
            
    # Display the original elevation dataset as a filled contour image
    fig = pyplot.figure(figsize = (12, 8))
    ax = fig.add_subplot(111)
    pyplot.contourf(elev, cmap = "viridis", 
            levels = list(range(0, 300, 25)))
    pyplot.title("Digital Elevation Model")
    cbar = pyplot.colorbar()
    pyplot.gca().set_aspect('equal', adjustable='box')
    pyplot.show()
                  
    # Copy a 2-D elevation matrix
    elev_copy = copy.deepcopy(elev)
    
    # Calculate the number of rows and columns in the matrix
    width = len(elev_copy) - 1
    height = len(elev_copy[0]) - 1
    
    # Loop through elevation cols and rows
    for row in elev:
        for value in row:
            
            # If the pixel is in the top left corner
            if (k == 0) and (l == 0):
                print("I'm here Top left")
                # Populates pixellist, whichpix function req the pixellist and
                # returns drop pixel ref and elevation change
                pixellist = [elev[l][k+1], elev[l+1][k+1], elev[l+1][k],
                             255, 255, 255, 255, 255]
                pixid, elevdeduct = D8framework4.whichpix(l, k, elev_copy, pixellist)
                if pixid % 2 == 0:
                    diag = True
                if pixid % 2 != 0:
                    diag = False
                # Flow Direction function req the pixellist + pixid and
                # returns the directional code
                directcode = D8framework4.flowdirection(l, k, diag, elev_copy,
                             pixellist, pixid, elevdeduct)
                # Updates the pixel value to directional code
                D8framework4.update(l, k, elev_copy, directcode)
                k+=1
            
            # If the pixel is in the top right corner
            elif (k == 299) and (l == 0):
                print("I'm here Top right")
                pixellist = [255, 255, elev[l][k-1], elev[l+1][k-1],
                             elev[l+1][k], 255, 255, 255]
                pixid, elevdeduct = D8framework4.whichpix(l, k, elev_copy, 
                                    pixellist)
                if pixid % 2 == 0:
                    diag = True
                if pixid % 2 != 0:
                    diag = False
                directcode = D8framework4.flowdirection(l, k, diag, elev_copy,
                             pixellist, pixid, elevdeduct)
                D8framework4.update(l, k, elev_copy, directcode)
                k+=1
            
            # If the pixel is in the bottom left corner
            elif (k == 0) and (l == 299):
                print("I'm here Bottom Left")
                pixellist = [elev[l][k+1], 255, 255, 255, 255, 255,
                             elev[l-1][k], elev[l-1][k+1]]
                pixid, elevdeduct = D8framework4.whichpix(l, k, elev_copy, pixellist)
                if pixid % 2 == 0:
                    diag = True
                if pixid % 2 != 0:
                    diag = False
                directcode = D8framework4.flowdirection(l, k, diag, elev_copy,
                             pixellist, pixid, elevdeduct)
                D8framework4.update(l, k, elev_copy, directcode)
                k+=1
            
            # If the pixel is in the bottom right corner
            elif (k == 299) and (l == 299):
                print("I'm here Bottom Right")
                pixellist = [255, 255, 255, 255, elev[l][k-1], elev[l-1][k-1],
                             elev[l-1][k], 255]
                pixid, elevdeduct = D8framework4.whichpix(l, k, elev_copy, pixellist)
                if pixid % 2 == 0:
                    diag = True
                if pixid % 2 != 0:
                    diag = False
                directcode = D8framework4.flowdirection(l, k, diag, elev_copy,
                             pixellist, pixid, elevdeduct)
                D8framework4.update(l, k, elev_copy, directcode)
                k+=1
                
                # Loop through the rows and values in the matrix and log2 + 1 not 0
                list_to_plot = []
                for inner_list in elev_copy:
                    list_to_plot.append([math.log(x, 2) if x else 0 for x in inner_list])
                # Display the flow direction dataset as an filled contour image
                fig = pyplot.figure(figsize = (12, 8))
                ax = fig.add_subplot(111)
                pyplot.contourf(list_to_plot, cmap = "rainbow", levels = list(range(0, 8)))
                pyplot.title("D8 Flow Direction")
                cbar = pyplot.colorbar()
                pyplot.gca().set_aspect('equal', adjustable='box')
                pyplot.show()
            
                # Write the results to a file
                # Opens csv file into reader, appends values to rowlist, rowlists to elevation
                with open('flowdirection.csv', 'w', newline="") as csv_file2:
                    writer = csv.writer(csv_file2)
                    writer.writerows(elev_copy)
                    csv_file2.close()
                
                # Calc model runtime and end program
                toc = time.perf_counter()
                print(f"Model ran in {toc - tic:0.4f} seconds", flush=True)
                csv_file.close()
                sys.exit("Program Complete")
                
            # If the pixel is on the top side
            elif (l == 0) and (0 < k < width-1):
                pixellist = [elev[l][k+1], elev[l+1][k+1], elev[l+1][k],
                             elev[l+1][k-1], elev[l-1][k-1], 255, 255, 255]
                pixid, elevdeduct = D8framework4.whichpix(l, k, elev_copy,
                                    pixellist)
                if pixid % 2 == 0:
                    diag = True
                if pixid % 2 != 0:
                    diag = False
                directcode = D8framework4.flowdirection(l, k, diag, elev_copy,
                             pixellist, pixid, elevdeduct)
                D8framework4.update(l, k, elev_copy, directcode)
                k+=1
            
            # If the pixel is on the bottom side
            elif (l == 299) and (0 < k < 299):
                pixellist = [elev[l][k+1], 255, 255, 255, elev[l][k-1],
                             elev[l-1][k-1], elev[l-1][k], elev[l-1][k+1]]
                pixid, elevdeduct = D8framework4.whichpix(l, k, elev_copy, pixellist)
                if pixid % 2 == 0:
                    diag = True
                if pixid % 2 != 0:
                    diag = False
                directcode = D8framework4.flowdirection(l, k, diag, elev_copy,
                             pixellist, pixid, elevdeduct)
                D8framework4.update(l, k, elev_copy, directcode)
                k+=1
            
            # If the pixel is on the left side
            elif (k == 0) and (0 < l < 299):
                pixellist = [elev[l][k+1], elev[l+1][k+1],
                elev[l+1][k], 255, 255, 255, elev[l-1][k], elev[l-1][k+1]]
                pixid, elevdeduct = D8framework4.whichpix(l, k, elev_copy, pixellist)
                if pixid % 2 == 0:
                    diag = True
                if pixid % 2 != 0:
                    diag = False
                directcode = D8framework4.flowdirection(l, k, diag, elev_copy,
                             pixellist, pixid, elevdeduct)
                D8framework4.update(l, k, elev_copy, directcode)
                k+=1
            
            # If the pixel is on the right side
            elif (k == 299) and (0 < l < 299):
                pixellist = [255, 255, elev[k][l+1], elev[k-1][l+1], elev[k-1][l],
                elev[l-1][k-1], elev[l-1][k], 255]
                pixid, elevdeduct = D8framework4.whichpix(l, k, elev_copy, pixellist)
                if pixid % 2 == 0:
                    diag = True
                if pixid % 2 != 0:
                    diag = False
                directcode = D8framework4.flowdirection(l, k, diag, elev_copy,
                             pixellist, pixid, elevdeduct)
                D8framework4.update(l, k, elev_copy, directcode)
                k+=1
                                              
            # If the pixel is in the middle and can form a 3 x 3 grid
            else:
                pixellist = [elev[l][k+1], elev[l+1][k+1], 
                             elev[l+1][k], elev[l+1][k-1],
                             elev[l][k-1], elev[l-1][k-1],
                             elev[l-1][k], elev[l+1][k-1]]
                pixid, elevdeduct = D8framework4.whichpix(l, k, elev_copy,
                                    pixellist)
                if pixid % 2 == 0:
                    diag = True
                if pixid % 2 != 0:
                    diag = False
                directcode = D8framework4.flowdirection(l, k, diag, elev_copy,
                             pixellist, pixid, elevdeduct)
                D8framework4.update(l, k, elev_copy, directcode)
                k+=1
                
        if k == 300:
            k = 0
            l+=1
        
        
        
                
    
    
    
    
    
            