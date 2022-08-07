import youtube_dl
from tqdm import tqdm

def download(vid):
	ydl_opts = {
	    'format': 'bestaudio/best',
	    # 'postprocessors': [{
	    #     'key': 'FFmpegExtractAudio',
	    #     'preferredcodec': 'mp3',
	    #     'preferredquality': '192',
	    # }],
    	# 'audioformat':'mp3',
	    'extractaudio':True,
	    'outtmpl': u'%(id)s.%(ext)s',
	}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	    ydl.download(['http://www.youtube.com/watch?v='+vid])

id='/m/015p6'

for file in ['eval_segments','balanced_train_segments','unbalanced_train_segments']:
	lines=open(file+'.csv').read().split('\n')
	vids=[]
	for line in lines:
		if id in line:
			elts=line.split(',')
			if len(elts)-3==1:
				vids.append(elts[0])
	for vid in tqdm(vids):
		download(vid)