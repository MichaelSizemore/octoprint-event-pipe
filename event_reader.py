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
		if event_in == 'test':
			ps = Popen(['python', '/home/pi/Testing/Adafruit_DotStar_Pi/strandtest.py'])
		elif event_in == 'z_change':
			ps = Popen(['python', '/home/pi/Testing/octoprint-event-pipe/z_change.py'])
		elif event_in == 'connected':
			ps = Popen(['python', '/home/pi/Testing/octoprint-event-pipe/connected.py'])
		elif event_in == 'print_started':
			ps = Popen(['python', '/home/pi/Testing/octoprint-event-pipe/print_started.py'])
		elif event_in == 'print_done':
			ps = Popen(['python', '/home/pi/Testing/octoprint-event-pipe/print_done.py'])
		elif event_in == 'print_cancelled':
			ps = Popen(['python', '/home/pi/Testing/octoprint-event-pipe/print_cancelled.py'])
                elif event_in == 'stop':
                        print 'Stopping'
                        print (ps.pid)
                        try:
                                ps.kill()
                        except:
                                print 'SOMETHING WENT WRONG!! COULDN"T KILL'
