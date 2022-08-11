# ids=['/m/015p6',
# '/m/02rlv9',
# '/m/07rkbfh',
# '/m/09x0r',
# '/m/05kq4',
# '/m/0cmf2',
# '/m/03m9d0z',
# '/m/0838f',
# '/m/03wwcy',
# '/m/0c3f7m',
# '/t/dd00002',
# '/m/0btp2',
# '/m/03p19w',
# '/m/0d31p',
# '/m/03kmc9',
# '/m/07qwf61',
# '/m/07q7njn',
# '/m/04rlf',
# '/m/03qtwd',
# '/m/04229',
# '/m/07qfr4h',
# '/m/0912c9',
# '/m/04229']
ids=[
    "_m_03qtwd",
    "_m_02rlv9",
    "_m_07rkbfh",
    "_m_07qfr4h",
    "_m_0c3f7m",
    "_m_03m9d0z",
    "_m_0912c9",
    "_m_04rlf",
    "_m_07pbtc8"
]

import youtube_dl
from tqdm import tqdm
import signal
import os
import sys

def handler(signum, frame):
	sys.exit(0)

def get_info(vid):
	ydl_opts = {}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	    dictMeta = ydl.extract_info(
	        "https://www.youtube.com/watch?v={sID}".format(sID=vid),
	        download=False)
	    return dictMeta['duration']#<60*10

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
	    'outtmpl': id+'/'+u'%(id)s.%(ext)s',
	}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	    ydl.download(['http://www.youtube.com/watch?v='+vid])

signal.signal(signal.SIGINT, handler)

print (sys.argv)
ids=ids[int(sys.argv[1]):int(sys.argv[2])]
print (ids)

def downloaded(files,vid):
	for file in files:
		if vid in file:
			return True
	return False

for id in ids:
	file_id = id.replace('/','_')
	if not os.path.exists(file_id):
		os.mkdir(file_id)
	
	files=os.listdir(file_id)
	n_files=len(files)
	target_n=600

	print ('TARGET ',target_n)
	for file in ['eval_segments','balanced_train_segments','unbalanced_train_segments']:
		lines=open(file+'.csv').read().split('\n')
		vids=[]
		for line in lines:
			if id in line:
				elts=line.split(',')
				if len(elts)-3==1:
					vids.append(elts[0])

		counter=0
		print ('vids ',len(vids))
		for vid in tqdm(vids):
			try :
				if get_info(vid) and not downloaded(files,vid):
					download(file_id,vid)
					counter+=1
				if counter == target_n:
					break
			except Exception as e:
				if 'unavailable' in str(e):
					print ('UNAVAILABLE')
				else:
					print (e)





