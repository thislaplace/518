#coding=utf-8
import numpy as np
import sklearn
import time
import pickle


data_path = 'E:\\code\\python3.x\\天池\\新浪微博\\Weibo Data\\weibo_train_data.txt'
result   = 'E:\\code\\python3.x\\天池\\新浪微博\\Weibo Data\\result.txt'
data_hash = dict()

''''' 
* datestr转换成secs 
* 将时间字符串转化为秒("2012-07-20 00:00:00"->1342713600.0) 
* 
'''  
def datestr2secs(datestr):
	time.strptime(datestr, '%Y-%m-%d %H:%M:%S')
	return time.mktime(time.strptime(datestr,'%Y-%m-%d %H:%M:%S'))
	

def read_data():
	global data_hash
	global reasult
	global data_path
	
	data_handle = open(data_path, 'rb')
	lines = data_handle.readlines()
	data_handle.close()
	
	for line in lines:
		line = line.strip().decode()
		line = line.split('\t')
		
		"""读取数据"""
		uid   = line[0]
		mid   = line[1]
		time  = str(line[2])
		forward_count = line[3]
		comment_count = line[4]
		like_count    = line[5]
		content       = line[6]
		
		second = datestr2secs(time)
		
		if not uid in data_hash:
			data_hash[uid] = []
		data_hash[uid].append([second, forward_count, comment_count, like_count])
	
	result_handle = open(result, 'wb')
	pickle.dump(data_hash, result_handle)
	result_handle.close()
	
read_data()
