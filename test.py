import pyautogui as pg
import time

CountClick = 0
while True:
    curX,curY = -1537,518
    pg.click(x=curX,y=curY)
    CountClick+=1
    print(CountClick)
    if(CountClick>1000):
        break
print("Finish")

#-1537   518 Your position
    
