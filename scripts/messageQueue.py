from javax.jms import *
from org.apache.activemq import ActiveMQConnectionFactory

class MyConsumer(MessageListener):
        def onMessage(self,m):
                try:
                        print "Received: " + repr(m.getText())
                except:
                        pass
        def run(self, brokerURL="tcp://192.168.1.103:61616", queueName="test"):
                factory=ActiveMQConnectionFactory(brokerURL)
                connection = factory.createConnection()
                connection.start()
                session = connection.createSession(False, Session.AUTO_ACKNOWLEDGE)
                destination = session.createQueue(queueName)
                consumer = session.createConsumer(destination)
                consumer.setMessageListener(self)



class MyProducer():
        factory, connection, session, producer = (None,None,None,None)
        def Producer(self, brokerURL="tcp://192.168.1.103:61616", queueName="test"):
                self.factory=ActiveMQConnectionFactory(brokerURL)
                self.connection=self.factory.createConnection()
                self.connection.start()
                self.session = self.connection.createSession(False, Session.AUTO_ACKNOWLEDGE);
                self.destination = self.session.createQueue(queueName);
                self.producer = self.session.createProducer(self.destination);
        def run(self):
                [self.message(u"Hello World!") for x in range(100)]
        def message(self, m):
                print "Sending: " + repr(m)
                message = self.session.createTextMessage(m)
                self.producer.send(message)
        def close(self):
                try:
                        self.connection.close()
                except:
                        pass



