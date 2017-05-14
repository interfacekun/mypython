text=$1
token=$2
url="http://tsn.baidu.com/text2audio?tex= $text &lan=zh&cuid=dlSwkVT56CHwmnZHA4fy3UGj&ctp=1&tok=$token"
wget -c "$url" -O audio.mp3 
mplayer audio.mp3 
rm audio.mp3

