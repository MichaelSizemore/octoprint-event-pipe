import os, time, sys, signal
from subprocess import Popen
led_library = "/home/pi/Testing/Adafruit_DotStar_Pi/strandtest.py"
pipe_name = "event-pipe"

def read_pipe():
	pipein = open(pipe_name, 'r')
 	line = pipein.readline()[:-1]
	if line != "":
		print 'Process %d got %s at %s' % (os.getpid(), line, time.time())
	return line

def handler(signum, frame):
        print 'I give up!'

signal.signal(signal.SIGINT, handler)

ps = Popen(['ls'])

while True:
	event_in = read_pipe()
	if event_in != "":
		print 'It checks out!'
                print 'Stopping'
                print (ps.pid)
                if (ps.pid):
                        try:
                                ps.terminate()
                        except:
                                print 'SOMETHING WENT WRONG!! COULDN"T KILL'

                if event_in == 'test':
			ps = Popen(['python', led_library, 'test'])
		elif event_in == 'ZChange':
			ps = Popen(['python', led_library, 'ZChange'])
		elif event_in == 'Startup':
			ps = Popen(['python', led_library, 'Startup'])
		elif event_in == 'Connected':
			ps = Popen(['python', led_library, 'Connected'])
		elif event_in == 'Disconnected':
			ps = Popen(['python', led_library, 'Disconnected'])
		elif event_in == 'PrintStarted':
			ps = Popen(['python', led_library, 'PrintStarted'])
                elif event_in == 'PrintFailed':
                        ps = Popen(['python', led_library, 'PrintFailed'])
                elif event_in == 'PrintDone':
                        ps = Popen(['python', led_library, 'PrintDone'])
                elif event_in == 'PrintCancelled':
                        ps = Popen(['python', led_library, 'PrintCancelled'])
                elif event_in == 'Home':
                        ps = Popen(['python', led_library, 'Home'])
                elif event_in == 'Paused':
                        ps = Popen(['python', led_library, 'Paused'])
