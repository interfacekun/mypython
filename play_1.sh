text=$1
url="http://tsn.baidu.com/text2audio?tex= $text &lan=zh&cuid=dlSwkVT56CHwmnZHA4fy3UGj&ctp=1&tok=24.121198f421dd509358a0a20b7b9a8372.2592000.1468414795.282335-8004519"
wget -c "$url" -O audio.mp3 
mplayer audio.mp3 


