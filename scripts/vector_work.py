from processing.core import PVector

class ball:
    def __init__(self):
        self.position = PVector(width/2, height/2)
        self.velocity = PVector(0,0)
        self.acceleration = PVector(-0.001,0.01)
        self.topspeed = 10
        self.color = color(255,255,0)
        self.size=20
    def draw(self):
        self.velocity.add(self.acceleration)
        self.velocity.limit(self.topspeed)
        self.position.add(self.velocity)
        noStroke()
        fill(self.color)
        #rotate(random(10)/10000.0)
        ellipse(self.position.x,self.position.y,self.size,self.size)
        self.checkEdges()
    def checkEdges(self):
        if self.position.x < 0:
            self.position.x = width
        if self.position.x > width:
            self.position.x = 0
        if self.position.y < 0:
            self.position.y = height
        if self.position.y > height:
            self.position.y = 0


noCursor()
b=[ball() for x in range(250)]
for x in b:
    x.position.x=float(width)/float(len(b)) * b.index(x)
    x.acceleration=PVector((random(100)-50) * 0.001,(random(100)-50)*0.001)
    x.color=color(random(255),0,0)
    x.topspeed=random(10)

def backgr():
    fill(255,255,255,10)
    rect(0,0,width,height)

drawlist=[backgr]
for x in b:
    drawlist.append(x.draw)
    

​
