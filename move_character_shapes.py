from pico2d import *
import os
import math

os.chdir('d:/2DGP/Lecture04_2D_Rendering')

def randerCharacter(x, y):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    delay(0.01)

open_canvas()

character = load_image('character.png')
grass = load_image('grass.png')

x = 400
y = 90

while True:
    while x < 750:
        randerCharacter(x, y)
        x += 2
    while y < 550:
        randerCharacter(x, y)
        y += 2
    while x >= 50:
        randerCharacter(x, y)
        x -= 2
    while y >= 90:
        randerCharacter(x, y)
        y -= 2
    while x < 400:
        randerCharacter(x, y)
        x += 2
    for i in range(270, -90, -1):  
        randerCharacter(x,y)
        x = math.cos(i / 360 * 2 * math.pi) * 200 + 400
        y = math.sin(i / 360 * 2 * math.pi) * 200 + 290
        
    
