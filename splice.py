ids=['/m/07pbtc8']

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

print (sys.argv)
ids=ids[int(sys.argv[1]):int(sys.argv[2])]
print (ids)

folder_id=0
for id in ids:
	nid=id.replace('/','_')
	fs_temp=os.listdir(nid)
	fs=[]
	for i in fs_temp:
		if '_out.wav' not in i and '.part' not in i:
			fs.append(i)

	for file in tqdm(fs):
		oname=file
		if '.m4a' in file:
			file=file[:-4]
		elif '.webm' in file:
			file=file[:-5]
		if not os.path.exists(os.path.join(nid,file+'_out.wav')):
			start,l=find(file)
			file=os.path.join(nid,file)
			oname=os.path.join(nid,oname)
			cmd = 'ffmpeg -ss '+str(start)+' -i "'+oname+'" -t '+str(l)+' "'+file+'_out.wav"'
			print (cmd)
			os.system(cmd)
			print ("FOLDER ",folder_id,len(ids))
	folder_id+=1


















