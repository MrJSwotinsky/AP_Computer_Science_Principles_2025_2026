# Underwater Bacground:
Rect(0,0,400,400, fill = 'lightSkyBlue')

# Face (No eyes - Eyes included w/mask):
Circle(200, 200,100, fill = 'yellow')
Circle(200, 190, 15)
Oval(200, 230, 100, 30)
Rect(150, 215, 100, 15, fill = 'yellow')

# Mask & Eyes:
Rect(140,130,120,60, fill = 'lightYellow', border = 'blue')
Circle(175, 160, 15)
Circle(225, 160, 15)

# Regulator:
Star(200, 240, 25, 10, fill = 'darkBlue', roundness = 90)
Oval(130, 220, 150, 50, border = 'darkBlue', borderWidth = 8, fill = None, rotateAngle = 20)
Rect(110, 190, 75,40, fill = 'yellow')
Circle(120, 192, 20, fill = 'yellow')
