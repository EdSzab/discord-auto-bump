import pyautogui as pg
from time import sleep
#discord icon at x 42   y 45

#the gang icon at x 845   y 665

#enter text at x 1255   y 779

#the actual code
pg.moveTo(42, 45) #moves to my discord spot
pg.click() #these two open discord
pg.click()
sleep(2) #waits to open
pg.moveTo(918, 696) #moves to the server icon and opens
pg.moveTo(1307, 817) #moves to typing bar
pg.click()


while True:
    #typing the text
    pg.press('!')
    pg.press('d')
    pg.press(' ')
    pg.press('b')
    pg.press('u')
    pg.press('m')
    pg.press('p')
    pg.press('enter')
    sleep(60 * 120);
