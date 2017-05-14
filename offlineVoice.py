#! /usr/bin/env python
import sys
import os
import fcntl
import thread
import commands
reload(sys)
sys.setdefaultencoding('utf8')
cmar='arecord -r 16000 -d 2 -D plughw:1 -f S16 /root/linux_voice/bin/wav/iflytek02.wav'
os.system(cmar)
cmre='export LD_LIBRARY_PATH=/root/linux_voice/libs/RaspberryPi/ && /root/linux_voice/bin/iat_sample'
(status, say) = commands.getstatusoutput(cmre)
#output = os.popen(cmre)
#say = output.read()
print "say:"+say
print say
def showSay():
	f=open('/root/gpio/say.txt','w')
	fcntl.flock(f, fcntl.LOCK_EX)
	f.write(say)
	fcntl.flock(f, fcntl.LOCK_UN)
showSay()
