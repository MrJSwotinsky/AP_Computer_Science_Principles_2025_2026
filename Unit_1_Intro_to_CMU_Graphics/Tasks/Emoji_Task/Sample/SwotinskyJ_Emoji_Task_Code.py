# Underwater Bacground:
Rect(0,0,400,400, fill = gradient('lightSkyBlue', 'blue', start = 'top'))

# Face (No eyes - Eyes included w/mask):
Circle(200, 200,100, fill = 'yellow')
Circle(200, 190, 15)
Oval(200, 230, 100, 30)
Rect(150, 215, 100, 15, fill = 'yellow')

# Mask & Eyes:
Line(112, 150, 150, 162, fill = 'darkBlue', lineWidth = 20)
Line(288, 150, 250, 162, fill = 'darkBlue', lineWidth = 20)
Rect(140, 130, 120, 60, fill = 'lightYellow', border = 'blue')
Circle(175, 160, 15)
Circle(225, 160, 15)

# Regulator:
Oval(130, 220, 150, 50, border = 'darkBlue', borderWidth = 8, fill = None, rotateAngle = 20)
Rect(110, 190, 75,40, fill = 'yellow')
Circle(120, 192, 20, fill = 'yellow')
Star(200, 240, 25, 10, fill = 'darkBlue', roundness = 90)
Label('SCUBA', 200, 232, font = 'montserrat', size = 10, fill = 'white', bold = True)
Label('Gear', 200, 245, font = 'caveat', size = 20, fill = 'white', italic = True)

# Fish
Polygon(300,100,320,80,340,80,355,95,370,80,370,120,355,105,340,120,320,120, fill = rgb(5, 250, 210))
Circle(316,96,4)
