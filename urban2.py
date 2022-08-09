import shutil
import sys
import os
from tqdm import tqdm

className=sys.argv[1]

if not os.path.exists('/gscratch/cse/jucha/audioset/UrbanSounds8K/UrbanSound8K/audio/'+className+'_subset'):
	os.mkdir('/gscratch/cse/jucha/audioset/UrbanSounds8K/UrbanSound8K/audio/'+className+'_subset')

fs=(os.listdir('/gscratch/cse/jucha/audioset/UrbanSounds8K/UrbanSound8K/audio/'+className))

for i in tqdm(range(600)):
	oname='/gscratch/cse/jucha/audioset/UrbanSounds8K/UrbanSound8K/audio/'+className+'/'+fs[i]
	nname='/gscratch/cse/jucha/audioset/UrbanSounds8K/UrbanSound8K/audio/'+className+'_subset/'+fs[i]
	shutil.copy(oname,nname)
	print (nname)