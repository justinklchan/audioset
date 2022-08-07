import youtube_dl
from tqdm import tqdm
import signal
import os
import sys

def handler(signum, frame):
	sys.exit(0)

def download(id,vid):
	ydl_opts = {
	    'format': 'bestaudio/best',
	    # 'postprocessors': [{
	    #     'key': 'FFmpegExtractAudio',
	    #     'preferredcodec': 'mp3',
	    #     'preferredquality': '192',
	    # }],
    	# 'audioformat':'mp3',
	    'extractaudio':True,
	    'outtmpl': id+u'%(id)s.%(ext)s',
	}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	    ydl.download(['http://www.youtube.com/watch?v='+vid])

signal.signal(signal.SIGINT, handler)


for id in ['/m/015p6']:
	if not os.path.exists('_'+id):
		os.mkdir('_'+id)
	for file in ['eval_segments','balanced_train_segments','unbalanced_train_segments']:
		lines=open(file+'.csv').read().split('\n')
		vids=[]
		for line in lines:
			if id in line:
				elts=line.split(',')
				if len(elts)-3==1:
					vids.append(elts[0])

		counter=0
		for vid in tqdm(vids):
			try :
				download(id,vid)
				counter+=1
				if counter == 350:
					break
			except:
				print ('err ',vid)