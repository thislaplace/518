# 518

用户(uid) 博文(mid) 发博时间(time) 转发数(forward_count) 评论数(comment_count) 赞数(like_count) 内容(content)
用户(uid)作为一级hash表的key值 value存储一个按时间排好序的list表
每一个博文(mid)又作为二级hash表的key值，value按顺序存储【转发数(forward_count) 评论数(comment_count) 赞数(like_count)】
博文内容不做处理