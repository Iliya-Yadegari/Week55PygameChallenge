import random

WIDTH = 800
HEIGHT = 600

ship_obj = Actor('playership1_blue',(300,550))
gem_obj = Actor('gemgreen',(300,100))

pause_switch = False

ship_obj.moving_switch = 'key'
gem_obj.score = 0

def draw():
    global pause_switch
    screen.fill('blue')
    ship_obj.draw()
    gem_obj.draw()

    screen.draw.text(f'score: {gem_obj.score}',(20,570),color = (71,255,14),fontsize = 50)

    if pause_switch == True:
        screen.fill((0,0,0))
        screen.draw.text('Pause',(300,300),color = (71,255,14),fontsize = 100)

    if gem_obj.top > 600:
        screen.fill((0,0,0))
        screen.draw.text('Game Over',(200,300),color = 'red',fontsize = 100)

def update():
    global pause_switch
    if pause_switch == False:
        movement()

        gem_obj.y += 3



    if ship_obj.colliderect(gem_obj):
        gem_obj.score += 1
        gem_obj.bottom = 0

        random_num = random.randint(20,780)

        gem_obj.x = random_num



def movement():
    global pause_switch

    if keyboard.left and ship_obj.left > 0:
        ship_obj.left -= 6

    if keyboard.right and ship_obj.right <= 800:
        ship_obj.right += 6

def on_key_down(key):
    global pause_switch
    if key == key.R and ship_obj.moving_switch == 'key':
        ship_obj.moving_switch = 'mouse'

    elif key == key.R and ship_obj.moving_switch == 'mouse':
        ship_obj.moving_switch = 'key'

    if key == key.ESCAPE and pause_switch == False:
        pause_switch = True
    elif key == key.ESCAPE and pause_switch == True:
        pause_switch = False

def on_mouse_move(pos):

    if ship_obj.moving_switch == 'mouse':
        ship_obj.x = pos[0]

