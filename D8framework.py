# -*- coding: utf-8 -*-
"""
Created on Mon May 17 16:00:08 2021

@author: Ciaran
"""

import math

def whichpix(l, k, elev_copy, pixellist):
    '''
    Takes in the values of l and k and elev_copy dataset, along with list of
    neighboring pixels with values. Loops through the pixellist and finds the
    and calculates a droplist of the differences between neighboring pixel
    elevations and original pixel elevation. Next, finds the lowest drop value, 
    the elevdeduct and notes the pixelid, returning both.
    '''
    droplist = []
    for pixel in pixellist:
        drop = pixel - elev_copy[l][k]
        droplist.append(drop)
    elevdeduct = min(droplist)
    pixid = 0
    for drop in droplist:
        if drop == elevdeduct:
            pixid = droplist.index(drop)
            droplist.clear()
            return pixid, elevdeduct
        
        
# Flow Direction function uses variables to calc largest % change in elev
# and updates the pixel to return the directional code          
def flowdirection(l, k, diag, elev_copy, pixellist, pixid , elevdeduct): 
    '''
    Takes in the value of l and k and the elev_copy dataset, along with the
    elededuct, pixid returned from whichpix function and the diagonal boolean
    and pixellist. Depending on the pixelid and boolean, the function calc 
    whether pixel is orthogonal or diagonal from original pixel and uses
    formula to calculate the max_drop, updating the pixel. 
    It also returns the flow direction value.
    '''          
            
    # Check value of pixelid to determine direction
    if pixid == 0:
        # If True, calc max drop using sqrt 2 and update pixel
        if diag == True:
            max_drop = elevdeduct / math.sqrt(2) * 100
            elev_copy[l][k] = max_drop
            return 1
        # If False, calc max drop and update pixel
        if diag == False:
            max_drop = elevdeduct / 1 * 100
            elev_copy[l][k] = max_drop
            return 1
    
    if pixid == 1:
        if diag == True:
            max_drop = elevdeduct / math.sqrt(2) * 100
            elev_copy[l][k] = max_drop
            return 2
        if diag == False:
            max_drop = elevdeduct / 1 * 100
            elev_copy[l][k] = max_drop
            return 2
        
    if pixid == 2:
        if diag == True:
            max_drop = elevdeduct / math.sqrt(2) * 100
            elev_copy[l][k] = max_drop
            return 4
        if diag == False:
            max_drop = elevdeduct / 1 * 100
            elev_copy[l][k] = max_drop
            return 4
        
    if pixid == 3:
        if diag == True:
            max_drop = elevdeduct / math.sqrt(2) * 100
            elev_copy[l][k] = max_drop
            return 8
        if diag == False:
            max_drop = elevdeduct / 1 * 100
            elev_copy[l][k] = max_drop
            return 8
        
    if pixid == 4:
        if diag == True:
            max_drop = elevdeduct / math.sqrt(2) * 100
            elev_copy[l][k] = max_drop
            return 16
        if diag == False:
            max_drop = elevdeduct / 1 * 100
            elev_copy[l][k] = max_drop
            return 16
        
    if pixid == 5:
        if diag == True:
            max_drop = elevdeduct / math.sqrt(2) * 100
            elev_copy[l][k] = max_drop
            return 32
        if diag == False:
            max_drop = elevdeduct / 1 * 100
            elev_copy[l][k] = max_drop
            return 32
        
    if pixid == 6:
        if diag == True:
            max_drop = elevdeduct / math.sqrt(2) * 100
            elev_copy[l][k] = max_drop
            return 64
        if diag == False:
            max_drop = elevdeduct / 1 * 100
            elev_copy[l][k] = max_drop
            return 64
        
    if pixid == 7:
        if diag == True:
            max_drop = elevdeduct / math.sqrt(2) * 100
            elev_copy[l][k] = max_drop
            return 128
        if diag == False:
            max_drop = elevdeduct / 1 * 100
            elev_copy[l][k] = max_drop
            return 128
        
def update(l, k, elev_copy, directcode):
    '''
    This simple function updates the pixel value with the directional code
    returned from the flow direction function
    '''
    elev_copy[l][k] = directcode