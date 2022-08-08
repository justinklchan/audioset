import os
# ids=['/m/015p6',
# '/m/02rlv9',
# '/m/07rkbfh',
# '/m/09x0r',
# '/m/05kq4',
# '/m/0cmf2',
# '/m/03m9d0z',
# '/m/0838f',
# '/m/03wwcy',
# '/m/0c3f7m',
# '/t/dd00002',
# '/m/0btp2',
# '/m/03p19w',
# '/m/0d31p',
# '/m/03kmc9',
# '/m/07qwf61',
# '/m/07q7njn',
# '/m/04rlf',
# '/m/03qtwd',
# '/m/04229']


for i in ids:
	ni=i.replace('/','_')
	fs=os.listdir(ni)
	if len(fs)<301:
		print (ni,len(fs))