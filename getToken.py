#! /usr/bin/env python
import base64
import json
import urllib2
apiKey="dlSwkVT56CHwmnZHA4fy3UGj"
secretKey="01a19cd0b0fd35c16f83c4d9107d4a5e"
auth_url="https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + apiKey + "&client_secret=" + secretKey;
res = urllib2.urlopen(auth_url)  
json_data = res.read().decode("utf-8")  
access_token = json.loads(json_data)['access_token']
print access_token