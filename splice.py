import os
import sys
from tqdm import tqdm

def find(file):
	for lookup in ['unbalanced_train_segments','eval_segments','balanced_train_segments']:
		lines=open(lookup+'.csv').read().split('\n')
		for line in lines:
			if file in line:
				print ('FOUND ',file)
				elts=line.split(',')
				return float(elts[1]),float(elts[2])-float(elts[1])

	print ('NOT FOUND ',file)

ids=['/m/015p6',
'/m/02rlv9',
'/m/07rkbfh',
'/m/09x0r',
'/m/05kq4',
'/m/0cmf2',
'/m/03m9d0z',
'/m/0838f',
'/m/03wwcy',
'/m/0c3f7m',
'/t/dd00002',
'/m/0btp2',
'/m/03p19w',
'/m/0d31p',
'/m/03kmc9',
'/m/07qwf61',
'/m/07q7njn',
'/m/04rlf',
'/m/03qtwd',
'/m/04229']

print (sys.argv)
ids=ids[int(sys.argv[1]):int(sys.argv[2])]
print (ids)

for id in tqdm(ids):
	nid=id.replace('/','_')
	fs_temp=os.listdir(nid)
	fs=[]
	for i in fs_temp:
		if '_out.wav' not in i and '.part' not in i:
			fs.append(i)

	for file in fs:
		if '.m4a' in file:
			file=file[:-4]
		elif '.webm' in file:
			file=file[:-5]
		if not os.path.exists(os.path.join(nid,file+'_out.wav')):
			start,l=find(file)
			file=os.path.join(nid,file)
			cmd = 'ffmpeg -ss '+str(start)+' -i "'+file+'.m4a" -t '+str(l)+' "'+file+'_out.wav"'
			print (cmd)
			os.system(cmd)



















