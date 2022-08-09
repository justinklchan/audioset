import shutil

className='car_horn'
lines=open('/gscratch/cse/jucha/audioset/UrbanSounds8K/UrbanSound8K/metadata/UrbanSound8K.csv').read().split('\n')[1:]
for line in lines:
	elts=line.split(',')
	if elts[-1]==className:
		fold=elts[-3]
		fid=elts[0]
		oname='/gscratch/cse/jucha/audioset/UrbanSounds8K/UrbanSound8K/metadata/audio/fold'+str(fold)+'/'+str(fid)
		nname='/gscratch/cse/jucha/audioset/UrbanSounds8K/UrbanSound8K/metadata/audio/'+className+'/'
		shutil.copy(oname,nname)
		print (oname,nname)
# 100032-3-0-0.wav,100032,0.0,0.317551,1,5,3,dog_bark
