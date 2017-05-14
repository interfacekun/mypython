#! /usr/bin/env python
import base64
import json
import urllib2
import sys
import os
import fcntl
import thread
reload(sys)
sys.setdefaultencoding('utf8')
cmar='arecord -r 16000 -d 2 -D plughw:1 -f S16 /root/mypython/nihao.wav'
os.system(cmar)
apiKey="dlSwkVT56CHwmnZHA4fy3UGj"
secretKey="01a19cd0b0fd35c16f83c4d9107d4a5e"
auth_url="https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + apiKey + "&client_secret=" + secretKey;
res = urllib2.urlopen(auth_url)  
json_data = res.read().decode("utf-8")  
access_token = json.loads(json_data)['access_token']
mac_address="b8:27:eb:cb:99:f3"
def baidu_asr(speech_file):
	with open(speech_file, 'rb') as f:
		speech_data = f.read()
	speech_base64=base64.b64encode(speech_data).decode('utf-8')
	speech_length=len(speech_data)
	data_dict = {'format':'wav', 'rate':16000, 'channel':1, 'cuid':mac_address, 'token':access_token, 'lan':'zh', 'speech':speech_base64, 'len':speech_length}
	json_data = json.dumps(data_dict).encode('utf-8')
	json_length = len(json_data)
	request = urllib2.Request(url='http://vop.baidu.com/server_api')
	request.add_header("Content-Type", "application/json")
	request.add_header("Content-Length", json_length)
	fs = urllib2.urlopen(url=request, data=json_data)
	result_str = fs.read().decode('utf-8')
	json_resp = json.loads(result_str)
	return json_resp
json_resp = baidu_asr("/root/mypython/nihao.wav")
str=json.dumps(json_resp['result'],ensure_ascii=False)
say=str[2:-3]
def showSay():
	f=open('/root/gpio/say.txt','w')
	fcntl.flock(f, fcntl.LOCK_EX)
	f.write(say)
	fcntl.flock(f, fcntl.LOCK_UN)
thread.start_new_thread(showSay,())
cm='nohup /root/mypython/shandy.py '+say+' > /dev/null 2>&1'
os.system(cm)
