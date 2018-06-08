#coding=utf-8
import numpy as np
import sklearn
import time
import pickle


data_path    = 'E:\\code\\python3.x\\天池\\新浪微博\\Weibo Data\\weibo_train_data.txt'
predict_path = 'E:\\code\\python3.x\\天池\\新浪微博\\Weibo Data\\weibo_predict_data.txt'
result       = 'E:\\code\\python3.x\\天池\\新浪微博\\Weibo Data\\result.txt'
out          = 'E:\\code\\python3.x\\天池\\新浪微博\\Weibo Data\\last_result.txt'
ignore_cnt = 2

def datestr2secs(datestr):
  time.strptime(datestr, '%Y-%m-%d %H:%M:%S')
  return time.mktime(time.strptime(datestr,'%Y-%m-%d %H:%M:%S'))
  

def getlistsum(_list):
  list_sum = 0
  for item in _list:
    list_sum += int(item)
  
  return list_sum

def get_average(_list, _index):
  list_len = len(_list)
  list_sum = 0
  for i in range(0, list_len):
    list_sum += int(_list[i][_index])
  
  return list_sum//list_len
  

def read_data():
  global reasult
  global data_path
  
  data_hash = dict()
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
  
  global ignore_cnt
  for key in list(data_hash.keys()):
    total_cnt = 0
    for item in data_hash[key]:
      total_cnt += getlistsum(item[1:4])
    if (total_cnt < ignore_cnt):
      data_hash.pop(key)
      
  result_handle = open(result, 'wb')
  pickle.dump(data_hash, result_handle)
  result_handle.close()
  

def predict():
  global result
  global out
  global predict_path
  
  out_handle = open(out, 'w+')
  result_handle = open(result, 'rb')
  data_hash = pickle.load(result_handle)
  result_handle.close()
  
  predict_handle = open(predict_path, 'rb')
  lines = predict_handle.readlines()
  
  key_list = list(data_hash.keys())
  for line in lines:
    line = line.decode()
    line = line.strip()
    line = line.split('\t')
    uid = line[0]
    mid = line[1]
    
    if uid not in key_list:
      out_handle.write("%s\t%s\t%d,%d,%d\n"%(uid, mid, 0, 0, 0))
    else:
      forward_cnt = get_average(data_hash[uid], 1)
      comment_cnt = get_average(data_hash[uid], 2)
      like_cnt    = get_average(data_hash[uid], 3)
      out_handle.write("%s\t%s\t%d,%d,%d\n"%(uid, mid, forward_cnt, comment_cnt, like_cnt))
    
  out_handle.close()
  
  

predict()
print("yuhao!!")