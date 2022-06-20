from tkinter import *
import tkinter as tk
import random
from win32api import GetSystemMetrics
root = tk.Tk()
    
 
 
width=GetSystemMetrics(0)
height=GetSystemMetrics(1)
 
 
x = root.winfo_x()
 
y = root.winfo_y()
block_left = False
block_up = False
def sus():
    global x,block_left,block_up,y
    while True:
       
        if (x > -1 and x < width and block_left == False):
            x += 10;
            block_left = False
        else:
            x -= 10;
            if (x > -1):
                block_left = True
            else:
                block_left = False
                
        if ( y > -1 and  y < height and block_up == False):
            y += 10
            block_up = False
                
        else:
            y -= 10;
            block_up = True
                
        if (y < -1):
            y += 20
            block_up = False
            
        if (x < -1):
            x += 20
            block_left = False
                
                
        print(x)
        root.geometry('%dx%d+%d+%d' % (100, 100, x, y))
        root.update()
      
        root.update()
 
root.after(1, sus)
root.mainloop()
 
print('sssssssssss')
 
