from javax.jms import *
from org.apache.activemq import ActiveMQConnectionFactory
import sys
sys.path.append('./Lib')
import os
print os.getcwd()
from exceptions import Exception
pyopen=open

for k in dir(P):
	if k == "open":
		print "skipping the clobber of open keyword"
	elif k[:8] == "ancestor":
		print "skipping: " + repr(k)
	elif k == "graphicsConfiguration":
		print "skipping: " + repr(k)
	elif k == "hierarchyChanged":
		print "skipping: " + repr(k)
	elif k == "locationOnScreen":
		print "skipping: " + repr(k)
	elif k == "maximumSize":
		print "skipping: " + repr(k)
	elif k == "minimumSize":
		print "skipping: " + repr(k)
	elif k == "mousePosition":
		print "skipping: " + repr(k)
	else :
		try:
			print "mapping: " + repr(k)
			exec(k+'=P.__getattribute__(\"'+k+'\")')
			print "mapped: " + repr(k)
		except:
			print "failed to map" + repr(k)

#del(P)
print os.getcwd()

#drawlist
drawlist=[]
def doDraw():
	for d in drawlist:
		try:
			d()
		except:
			pass

def goExec(x,g,l):
	exec(x,g,l)


class MyProducer():
	factory, connection, session, producer = (None,None,None,None)
	def Producer(self, brokerURL="tcp://192.168.1.103:61616", queueName="processing-output"):
		self.factory=ActiveMQConnectionFactory(brokerURL)
		self.connection=self.factory.createConnection()
		self.connection.start()
		self.session = self.connection.createSession(False, Session.AUTO_ACKNOWLEDGE);
		self.destination = self.session.createQueue(queueName);
		self.producer = self.session.createProducer(self.destination);
	def message(self, m):
#		print "Sending: " + repr(m)
		message = self.session.createTextMessage(m)
		self.producer.send(message)
	def close(self):
		try:
			self.connection.close()
		except:
			pass



class MyConsumer(MessageListener):
	def setNS(self,g,l,p,e):
		self.g=g
		self.l=l
		self.p=p
		self.execFunc=e
        def onMessage(self,m):
        	result=None
#                try:
#                        print "Received: " + repr(m.getText())
#                except:
#                        pass
                try:
                	result=self.execFunc(m.getText(),self.g,self.l)
                except:
                	result='\n'.join([repr(sys.exc_info()[1].__class__),sys.exc_info()[1].message])
		if result != None:
			self.p.message(result)
        def run(self, brokerURL="tcp://192.168.1.103:61616", queueName="processing"):
                factory=ActiveMQConnectionFactory(brokerURL)
                connection = factory.createConnection()
                connection.start()
                session = connection.createSession(False, Session.AUTO_ACKNOWLEDGE)
                destination = session.createQueue(queueName)
                consumer = session.createConsumer(destination)
                consumer.setMessageListener(self)


pro=MyProducer()
pro.Producer()
executer=MyConsumer()
executer.setNS(globals(),locals(),pro,goExec)
executer.run()
evaler=MyConsumer()
evaler.setNS(globals(),locals(),pro,eval)
evaler.run(queueName="processing-eval")
print os.getcwd()

