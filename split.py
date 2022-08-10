import os
import shutil
# for c in ['air_conditioner','car_horn','dog_bark','drilling','engine_idling','jackhammer','siren']:
# 	fs=sorted(os.listdir(c+'_subset'))

# 	ufiles=[]
# 	for i in fs:
# 		if '.wav' in i:
# 			elts=i.split('-')[0]
# 			if elts not in ufiles:
# 				print 
# 				ufiles.append(elts)

# 	print (c,len(ufiles))

label_map={
	'_m_015p6':'Bird',
	'_t_dd00002':'Baby',
	'_m_0d31p':'Vacuum',
	'_m_05kq4':'Ocean'
}

fout=open('/gscratch/cse/jucha/FSDKaggle2018_audioset/FSDKaggle2018.meta/train_post_competition.csv','a')
od='/gscratch/cse/jucha/audioset/curated/'
nd='/gscratch/cse/jucha/FSDKaggle2018_audioset/FSDKaggle2018.train/'
for c in ['_m_015p6','_t_dd00002','_m_0d31p','_m_05kq4']:
	fs=sorted(os.listdir(od+c))
	train=fs[:int(len(fs)*.9)]
	print (len(train))
	for i in train:
		oname=od+c+'/'+i
		nname=nd+c+'/'+i
		# shutil.copy(oname,nname)
		text=i+','+label_map[c]+',1,0,attribution\n'
		# fout.write (text)
		print (oname)
		print (nname)
		print (text)
	# fff81f55.wav,Cough,1,19117,Attribution
fout.close()



























