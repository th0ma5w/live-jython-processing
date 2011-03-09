white = lambda : background(255)
black = lambda : background(0)
rando = lambda r,g,b : fill(random(r),random(g),random(b))


def randCirc():
        rando(255,255,0)
        ellipse(random(width),random(height),random(20),random(20))

frameRate(90)
noCursor()
noStroke()

def clearQueue():
    global drawlist
    drawlist=[]

savvy = lambda : save("/home/media/screenShot.png")

drawlist=[randCirc for x in range(100)]
drawlist.insert(0,black)
#drawlist.insert(0,white)
drawlist.append(savvy)
drawlist.append(clearQueue)

pro.message(repr(random(255)))

