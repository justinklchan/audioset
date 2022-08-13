import os
import shutil
import itertools
from tqdm import tqdm
import random
import sys

random.seed(1)

def subsetsum(array,num):
    if num == 0 or num < 1:
        return None
    elif len(array) == 0:
        return None
    else:
        if array[0] == num:
            return [array[0]]
        else:
            with_v = subsetsum(array[1:],(num - array[0])) 
            if with_v:
                return [array[0]] + with_v
            else:
                return subsetsum(array[1:],num)

def closest(my_list, my_number):
    l=[]
    for i in tqdm(range(1,len(my_list)+1)):
        for k in itertools.combinations(my_list, i):
            l.append([k, sum(k)])
    l=[i for i in l if i[1]<=my_number]
    l.sort(key=lambda x:x[1])
    return l[-1]

def split_urban():
	fout_train=open('/gscratch/cse/jucha/FSDKaggle2018_audioset/FSDKaggle2018.meta/train_post_competition.csv','a')
	fout_test=open('/gscratch/cse/jucha/FSDKaggle2018_audioset/FSDKaggle2018.meta/test_post_competition_scoring_clips.csv','a')

	od='/gscratch/cse/jucha/audioset/curated/'
	nd_train='/gscratch/cse/jucha/FSDKaggle2018_audioset/FSDKaggle2018.audio_train/'
	nd_test='/gscratch/cse/jucha/FSDKaggle2018_audioset/FSDKaggle2018.audio_test/'
	label_map={
		'air_conditioner':'Air_conditioner',
		'car_horn':'Car_horn',
		'drilling':'Drilling',
		'engine_idling':'Engine_idling',
		'jackhammer':'Jackhammer',
		'siren':'Siren'
	}
	
	for c in label_map.keys():
		fs=sorted(os.listdir(od+c+'_subset'))

		ufiles={}
		for i in fs:
			if '.wav' in i:
				elts=i.split('-')[0]
				if elts not in ufiles.keys():
					ufiles[elts]=0
				ufiles[elts]+=1

		target=int(sum(ufiles.values())*.1)

		train_keys = list(ufiles.keys())
		test_keys = []
		vals = list(ufiles.values())
		random.shuffle(vals)

		subset=subsetsum(vals, target)

		# get back the keys
		for num in subset:
			for i,(k,v) in enumerate(ufiles.items()):
				# print (k,v,num)
				if v==num and k in train_keys:
					test_keys.append(k)
					train_keys.remove(k)

		for i in fs:
			if '.wav' in i:
				elts=i.split('-')[0]
				print (elts)
				if elts in train_keys and not os.path.exists(nd_train+i):
					# print ('train ',i)
					oname=od+c+'_subset/'+i
					nname=nd_train+i
					# print (oname,nname)
					shutil.copy(oname,nname)
					fout_train.write(i+','+label_map[c]+',1,0,Attribution\n')
				if elts in test_keys and not os.path.exists(nd_test+i):
					# print ('test ',i)
					oname=od+c+'_subset/'+i
					nname=nd_test+i
					# print (oname,nname)
					shutil.copy(oname,nname)
					fout_test.write(i+','+label_map[c]+',1,0,Attribution\n')
		# break

	fout_train.close()
	fout_test.close()

def split_yt():
	label_map={
		'_m_015p6':'Bird',
		'_t_dd00002':'Baby',
		'_m_0d31p':'Vacuum',
		'_m_05kq4':'Ocean',
		'_m_0c3f7m':'Fire_alarm',
		'_m_02rlv9':'Motorboat',
		'_m_04rlf':'Music',
		'_m_03m9d0z':'Wind',
		'_m_03qtwd':'Crowd'
		'_m_07pbtc8':'Walking'
	}

	fout=open('/gscratch/cse/jucha/FSDKaggle2018_audioset/FSDKaggle2018.meta/test_post_competition_scoring_clips.csv','a')
	od='/gscratch/cse/jucha/audioset/curated/'
	nd='/gscratch/cse/jucha/FSDKaggle2018_audioset/FSDKaggle2018.audio_test/'
	for c in label_map.keys():
		fs=sorted(os.listdir(od+c))
		test=fs[int(len(fs)*.9):]
		print (len(test))
		for i in test:
			oname=od+c+'/'+i
			nname=nd+i
			shutil.copy(oname,nname)
			text=i+','+label_map[c]+',1,0,attribution\n'
			fout.write (text)
	fout.close()

	fout=open('/gscratch/cse/jucha/FSDKaggle2018_audioset/FSDKaggle2018.meta/train_post_competition.csv','a')
	od='/gscratch/cse/jucha/audioset/curated/'
	nd='/gscratch/cse/jucha/FSDKaggle2018_audioset/FSDKaggle2018.audio_train/'
	for c in label_map.keys():
		fs=sorted(os.listdir(od+c))
		train=fs[:int(len(fs)*.9)]
		print (len(train))
		for i in train:
			oname=od+c+'/'+i
			nname=nd+i
			shutil.copy(oname,nname)
			text=i+','+label_map[c]+',1,0,attribution\n'
			fout.write (text)
	fout.close()

if int(sys.argv[1])==1:
	split_yt()
elif int(sys.argv[1])==2:
	split_urban()

























