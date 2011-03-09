rotationv=0

noSmooth()

background(60)

def blackbg():
    noStroke()
    fill(60,5)
    rect(0,0,screenWidth,screenHeight)

def doRotate():
    translate(screenWidth/2,screenHeight/2)
    rotate(radians(rotationv))

def drawcircle(x,y,s):
    noStroke()
    fill(0,255,0)
    ellipseMode(CENTER)
    ellipse(x,y,s,s)


def updateRotate():
    global rotationv
    rotationv = rotationv + 2
    if rotationv > 360:
        rotationv = 0


blackbg()

circgrid = lambda : [[drawcircle(x+(screenWidth/10/2)-(screenWidth/2),y-(screenHeight/2),5) for x in range(0,screenWidth,screenWidth/10)] for y in range(0,screenHeight,screenHeight/10)]
    
drawlist=[blackbg, doRotate, circgrid, updateRotate]

​
