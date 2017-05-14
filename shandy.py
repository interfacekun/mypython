#! /usr/bin/env python
import json
import urllib
import urllib2
import sys
import random
import os
import fcntl
import thread
reload(sys)  
sys.setdefaultencoding('utf8')
def baidu_asr():
	userID=random.randint(1, 100)
	#mykey="ecb4976819bb565ac65916070cd425f8"
	mykey="2ba52d0c1f3341d18be2e48fc4405b3d"
	msg=sys.argv[1]
	#jdata = {"key":"ecb4976819bb565ac65916070cd425f8","info":msg}
	#json_data = json.dumps(jdata).decode('utf-8')
	#request = urllib2.Request('http://www.tuling123.com/openapi/api',json_data)
	url='http://www.tuling123.com/openapi/api'
	
	#request.get_method = lambda:'POST'
	#url='http://www.tuling123.com/openapi/api?key='+mykey+'&info='+msg+'&userid='+str(userID)
	#request.add_header('Content-Type', 'application/json')
	json_data = urllib.urlencode({"key":mykey,"info":msg,"userid":str(userID)})
	fs=urllib2.urlopen(url=url, data=json_data)
	#fs = urllib2.urlopen(url)
	result_str = fs.read().decode('utf-8')
	json_resp = json.loads(result_str,encoding="utf-8")
	return json_resp
json_resp = baidu_asr()
#print json.dumps(json_resp["text"],ensure_ascii=False)
say=json_resp["text"]
def showSay():
	f=open('/root/gpio/say.txt','w')
	fcntl.flock(f, fcntl.LOCK_EX)
	f.write(say)
	fcntl.flock(f, fcntl.LOCK_UN)
thread.start_new_thread(showSay,())
apiKey="dlSwkVT56CHwmnZHA4fy3UGj"
secretKey="01a19cd0b0fd35c16f83c4d9107d4a5e"
auth_url="https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + apiKey + "&client_secret=" + secretKey;
res = urllib2.urlopen(auth_url)  
json_data = res.read().decode("utf-8")  
access_token = json.loads(json_data)['access_token']
cm='nohup /root/mypython/play.sh '+say+' '+access_token+' > /dev/null 2>&1'
os.system(cm)


