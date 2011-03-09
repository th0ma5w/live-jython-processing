from flask import Flask, request
import stomp, difflib, werkzeug

CONNECTION=[('192.168.1.107', 61613)]

MESSAGE = ""
DIFF=[]
LAST=[]

class MyListener(object):
	def on_error(self,headers,message):
		pass
	def on_message(self, headers, message):
		global MESSAGE
		MESSAGE = message


conn=stomp.Connection(host_and_ports=CONNECTION)
conn.set_listener('', MyListener())
conn.start()
conn.connect()
conn.subscribe(destination='/queue/processing-output', ack='auto')


app = Flask(__name__)

@app.route('/lastMessage')
def lastMsg():
	global MESSAGE
	return """
<html>
<head>
<meta http-equiv="refresh" content="5">
</head>
<body>
""" + MESSAGE + """
</body>
</html>

"""

#@app.route('/last')
#def last():
#	global LAST
#	return werkzeug.Response("\n".join(LAST),content_type="text/plain; charset=utf-8")

#@app.route('/diff')
#def diff():
#	global DIFF
#	return werkzeug.Response("\n".join(DIFF),content_type="text/plain; charset=utf-8")


#	code=code.splitlines()
#	d=difflib.Differ()
#	thisdiff = d.compare(LAST,code)
#	LAST=code
#	for x in thisdiff:
#		if (x[0]=="+") or (x[0]=="-") or (x[0]=="@"):
#			DIFF.append(x)

@app.route('/go',methods=['POST'])
def go():
	global LAST,DIFF
	code=request.form['code']
	conn.send(code,destination='/queue/processing')
	return ""

@app.route('/eval',methods=['POST'])
def evaluate():
	global LAST,DIFF
	code=request.form['code']
	conn.send(code,destination='/queue/processing-eval')
	return ""

@app.route('/shutdown')
def shutdown():
	conn.disconnect()
	app.exit()


app.run(host="0.0.0.0")

