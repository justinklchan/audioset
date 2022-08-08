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
'/m/04229',
'/m/07qfr4h',
'/m/0912c9',
'/m/04229']

import os

lines=open('class_labels_indices.csv').read().split('\n')

mmap={}
for i in ids:
	name=""
	for j in lines:
		if i in j:
			name=j.split(',')[-1]
			break

	ni=i.replace('/','_')
	fs=os.listdir(ni)
	fs2=[]
	for i in fs:
		if '.wav' not in i:
			fs2.append(i)
		mmap[ni+","+name]=len(fs2)

smap=dict(sorted(mmap.items(), reverse=True, key=lambda item: item[1]))
for i in smap.keys():
	print (i,smap[i])

print (len(smap.keys()))




