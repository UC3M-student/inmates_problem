# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 21:30:03 2022

@author: V.M
"""

import random 
import numpy as np


a = np.arange(1, 101) # prisoners and boxnumbers

def prisoners_puntuation(list1,list2):
    
    boxes_game = []
    
    for i in range(100):
        boxes_game.append(list1[i])
        boxes_game.append(list2[i])
    
    boxes_game = np.array_split(boxes_game, 100)
    
    points = 1 
    
    for w in range(1,101):
        tt = boxes_game[w-1][1]
        
        for z in range(1,52):
            
            if tt == w:
                break
            
            elif z == 51:
                points = 0

                break
            
            else:
                tt = boxes_game[tt-1][1]
        if points == 0:
            break
        
        
    return int(points)
    



percentage = 0

for i in range(10000):
    
    b = random.sample(range(1,101), 100) # inside_box_number
    percentage += prisoners_puntuation(a, b)


print(percentage/10000)


    

    












