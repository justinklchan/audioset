import shutil
import sys
import os
className=sys.argv[1]

if not os.path.exists('/gscratch/cse/jucha/audioset/UrbanSounds8K/UrbanSound8K/audio/'+className):
	os.mkdir('/gscratch/cse/jucha/audioset/UrbanSounds8K/UrbanSound8K/audio/'+className)

lines=open('/gscratch/cse/jucha/audioset/UrbanSounds8K/UrbanSound8K/metadata/UrbanSound8K.csv').read().split('\n')[1:]
for line in lines:
	elts=line.split(',')
	if elts[-1]==className:
		print (line)
		fold=elts[-3]
		fid=elts[0]
		foreground=int(elts[-4])
		if foreground==1:
			oname='/gscratch/cse/jucha/audioset/UrbanSounds8K/UrbanSound8K/audio/fold'+str(fold)+'/'+str(fid)
			nname='/gscratch/cse/jucha/audioset/UrbanSounds8K/UrbanSound8K/audio/'+className+'/'
			shutil.copy(oname,nname)
			print (oname,nname)
# 100032-3-0-0.wav,100032,0.0,0.317551,1,5,3,dog_bark
