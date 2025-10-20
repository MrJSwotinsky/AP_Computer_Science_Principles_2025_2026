# Draw maze background:
Rect(0, 0, 400, 340, fill = 'lightGrey')


# Draw maze runner:
maze_runner = Circle(25, 25, 10, fill = 'Gold')
maze_runner.distance_travelled = 0


# Draw maze:
Label('Start', 25, 25)
Label('Finish', 370, 315)
Line(50, 10, 390, 10)
Line(390, 10, 390, 290)
Line(10, 330, 350, 330)
Line(10, 50, 10, 330)
Line(10, 50, 180, 50)
Line(220, 50, 390, 50)
Line(50, 90, 350, 90)
Line(350, 90, 350, 240)
Line(50, 290, 390, 290)
Line(310, 90, 310, 290)
Line(50, 130, 260, 130)
Line(10, 170, 220, 170)
Line(260, 130, 260, 210)
Line(50, 250, 260, 250)
Line(50, 250, 50, 290)
Line(10, 210, 260, 210)


# Accept left, top, and shape as arguments, and draw a shape-shaped button with the its top-left corner at top and left:
def draw_button(left,top, shape):
    if shape == 'Square':
        Rect(left, top, 40, 40, fill = 'lightGrey')
        Polygon(left, top, left + 40, top, left + 30, top + 10, left + 10, top + 10, fill = 'paleGoldenRod')
        Polygon(left, top, left, top + 40, left + 10, top + 30, left + 10, top + 10, fill = 'gold')
        Polygon(left + 40, top, left + 40, top + 40, left + 30, top + 30, left + 30, top + 10, fill = 'gold')
        Polygon(left, top + 40, left + 40, top + 40, left + 30, top + 30, left + 10, top + 30, fill = 'paleGoldenRod')
    elif shape == 'Circle':
        Circle(left + 20, top + 20, 20, fill = gradient('lightGoldenRodYellow', 'gold', start = 'top-left'))
        Circle(left + 20, top + 20, 12, fill = 'lightGrey')
    else:
        pass


# Draw button panel background:
panel = Rect(0, 340, 400, 60, fill = 'lavender', visible = False)


# Draw buttons and for each button add a label (L,R,U, or D) and a white cover that can change opacity to make the button look pressed:
left_button = draw_button(10, 350, 'Circle')
left_button_label = Label('L', 30, 370)
left_button_cover = Rect(10, 350, 50, 50, fill = 'white', opacity = 0)

right_button = draw_button(85, 350, 'Circle')
right_button_label = Label('R', 105, 370)
right_button_cover = Rect(85, 350, 50, 50, fill = 'white', opacity = 0)

up_button = draw_button(160, 350, 'Circle')
up_button_label = Label('U', 180, 370)
up_button_cover = Rect(160, 350, 50, 50, fill = 'white', opacity = 0)

down_button = draw_button(235, 350, 'Circle')
down_button_label = Label('D', 255, 370)
down_button_cover = Rect(235, 350, 50, 50, fill = 'white', opacity = 0)


# Draw pointer:
pointer = Polygon(200, 200, 220, 210, 210, 220, fill = 'red')


# Draw distance display:
Label('Distance Travelled:', 340, 360)
distance = Label(maze_runner.distance_travelled, 340, 375)
Label = Label('px', 340, 390)


# Drag the maze runner and the pointer as the mouse is dragged:
def onMouseDrag(mouseX, mouseY):
        # Only allow the mazerunner to be dragged while above the buttons:
        if pointer.centerY < 350:
            maze_runner.centerX = mouseX
            maze_runner.centerY = mouseY
        else: 
            pass
        pointer.centerX = mouseX
        pointer.centerY = mouseY
  

# Drag the pointer as the mouse moves.      
def onMouseMove(mouseX, mouseY):
        pointer.centerX = mouseX
        pointer.centerY = mouseY
        if panel.hits(mouseX, mouseY):
            panel.visible = True
        else:
            panel.visible = False


# When the mouse is pressed, check whether or not the pointer hits any button.  
# If it is on a button, change that button's cover to 50% opacity to make it look pressed.
# Then move the maze runner 10 units in that direction, and update the distance travelled.
# If the pointer does not hit any button, do nothing:
def onMousePress(mouseX, mouseY):
    if pointer.hitsShape(left_button_cover):
        left_button_cover.opacity = 50
        maze_runner.centerX -= 10
        maze_runner.distance_travelled += 10
    elif pointer.hitsShape(right_button_cover):
        right_button_cover.opacity = 50
        maze_runner.centerX += 10
        maze_runner.distance_travelled += 10
    elif pointer.hitsShape(up_button_cover):
        up_button_cover.opacity = 50
        maze_runner.centerY -= 10
        maze_runner.distance_travelled += 10
    elif pointer.hitsShape(down_button_cover):
        down_button_cover.opacity = 50
        maze_runner.centerY += 10
        maze_runner.distance_travelled += 10
    else:
        pass
    distance.value = maze_runner.distance_travelled
 

# When a key is pressed, check whether or not it was the left, right, up, or down arrow key..  
# If it is the left, right, up, or down arrow key, change that button's cover to 50% opacity to make it look pressed.
# Then, move the maze runner 10 units in that direction, and update the distance travelled.
# If the pointer does not hit any button, do nothing:    
def onKeyPress(key):
    if key == 'left':
        left_button_cover.opacity = 50
        maze_runner.centerX -= 10
        maze_runner.distance_travelled += 10
    elif key == 'right':
        right_button_cover.opacity = 50
        maze_runner.centerX += 10
        maze_runner.distance_travelled += 10
    elif key == 'up':
        up_button_cover.opacity = 50
        maze_runner.centerY -= 10
        maze_runner.distance_travelled += 10
    elif key == 'down':
        down_button_cover.opacity = 50
        maze_runner.centerY += 10
        maze_runner.distance_travelled += 10
    else:
        pass
    distance.value = maze_runner.distance_travelled


# When the mouse is released, change all button's covers to 0% opacity to make them look not un-pressed:    
def onMouseRelease(mouseX, mouseY):
    left_button_cover.opacity = 0
    right_button_cover.opacity = 0
    up_button_cover.opacity = 0
    down_button_cover.opacity = 0
    

# When a key is released, change all button's covers to 0% opacity to make them look not un-pressed:     
def onKeyRelease(key):
    left_button_cover.opacity = 0
    right_button_cover.opacity = 0
    up_button_cover.opacity = 0
    down_button_cover.opacity = 0
