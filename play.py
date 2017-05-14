import os
import sys
cm='nohup /root/mypython/play.sh '+sys.argv[1]+' > /dev/null 2>&1'
os.system(cm)
#os.system('rm nohup.out')
