#coding=utf-8
import numpy as np
import pandas as pd
import sklearn

# 用户(uid) 博文(mid) 发博时间(time) 转发数(forward_count) 评论数(comment_count) 赞数(like_count) 内容(content)


file_handle = open('E:\\code\\python3.x\\天池\\新浪微博\\Weibo Data\\weibo_predict_data.txt', 'rb')
result_handle = open('E:\\code\\python3.x\\天池\\新浪微博\\Weibo Data\\result.txt', 'w')
lines = file_handle.readlines()
data = list()
for line in lines:
	line = line.strip().decode()
	line = line.split('\t')
	line = line[:2]
	data.append(line)
file_handle.close()

for line in data:
	result_handle.write(line[0]+'\t'+line[1]+'\t0'+',0,0\n')

result_handle.close()