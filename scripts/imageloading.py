

drawlist=[]

import hashlib,urllib2

u="http://www.google.com/intl/en_ALL/images/srpr/logo1w.png"
f=urllib2.urlopen(u)
g=f.read()
thehash = hashlib.md5(u).hexdigest()
h=pyopen(thehash+".png",'wb')
h.write(g)
f.close()
h.close()

im=loadImage(thehash+".png")

image(im,0,0)


