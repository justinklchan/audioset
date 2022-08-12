# ids=[
# # '/m/015p6',
# # '/m/02rlv9',
# '/m/07rkbfh',
# '/m/09x0r',
# # '/m/05kq4',
# # '/m/0cmf2',
# '/m/03m9d0z',
# # '/m/0838f',
# '/m/03wwcy',
# '/m/0c3f7m',
# # '/t/dd00002',
# '/m/0btp2',
# '/m/03p19w',
# # '/m/0d31p',
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
	# "/m/015p6",
	# "/t/dd00002",
	# "/m/0d31p",
	# "/m/0cmf2",
	# "/m/0838f",
	# "/m/05kq4",

    "_m_03qtwd",
    # "_m_02rlv9",
    "_m_07rkbfh",
    "_m_07qfr4h",
    # "_m_0c3f7m",
    "_m_03m9d0z",
    "_m_04rlf",
    "_m_07pbtc8",
    '_m_05kq4'
]

namemap={
	"_m_015p6":"bird",
	"_t_dd00002":"baby",
	"_m_0d31p":"vacuum",
	"_m_0cmf2":"airplane",
	"_m_0838f":"water",
	"_m_05kq4":"ocean",
	"_m_03qtwd":"crowd",
    "_m_02rlv9":"motorboat",
    "_m_07rkbfh":"chatter",
    "_m_07qfr4h":"speech",
    "_m_0c3f7m":"fire alarm",
    "_m_03m9d0z":"wind",
    "_m_04rlf":"music",
    "_m_07pbtc8":"walk"
}

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
	print (i,namemap[i.split(',')[0]],smap[i])

print (len(smap.keys()))



