import stomp

CONNECTION=[('192.168.1.103', 61613)]

class MyListener(object):
    def on_error(self, headers, message):
        print 'ERROR %s' % message
    def on_message(self, headers, message):
        print message

conn=stomp.Connection(host_and_ports=CONNECTION)
conn.set_listener('', MyListener())
conn.start()
conn.connect()
conn.subscribe(destination='/queue/processing-output', ack='auto')
go = lambda x: conn.send(x,destination='/queue/processing')
evalu = lambda x: conn.send(x,destination='/queue/processing-eval')

#go('noCursor()')
#[([go('background(255,0,'+str(x)+')') for x in range(0,255,10)],[go('background(0,'+str(x)+',255)')  for x in range(0,255,10)]) for z in range(5)]

