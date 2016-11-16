import os, time, sys
from subprocess import Popen
pipe_name = "event-pipe"

def read_pipe():
	pipein = open(pipe_name, 'r')
 	line = pipein.readline()[:-1]
	if line != "":
		print 'Process %d got %s at %s' % (os.getpid(), line, time.time())
	return line

while True:
	event_in = read_pipe()
	if event_in != "":
		print 'It checks out!'
		if event_in == 'z_change':
			ps = Popen(['python', '/home/pi/Testing/Adafruit_DotStar_Pi/strandtest.py'])
                elif event_in == 'stop':
                        print 'Stopping'
                        print (ps.pid)
                        ps.kill()
#                       try:
#                        ps.kill()
 #                       os.kill(ps.pid(),0)
 #                       except:
 #                               pass
                        
