# -*- coding: utf-8 -*-
import oss2
from oss2.credentials import EnvironmentVariableCredentialsProvider
import os

# 这里填写你的 OSS_ACCESS_KEY_ID 和 OSS_ACCESS_KEY_SECRET
os.environ['OSS_ACCESS_KEY_ID'] = ''
os.environ['OSS_ACCESS_KEY_SECRET'] = ''


auth = oss2.ProviderAuth(EnvironmentVariableCredentialsProvider())
# 这里改成你的
bucket = oss2.Bucket(auth, 'https://oss-cn-chengdu.aliyuncs.com', 'sourcedream-cloud')
# 填写Object完整路径，完整路径中不包含Bucket名称，例如testfolder/exampleobject.txt。
# 
# bucket.get_object_to_file('testfolder/exampleobject.txt', 'D:\\localpath\\examplefile.txt')

for obj in oss2.ObjectIterator(bucket):
    # 下面都是在判断文件是否存在 不存在就新建
    dirStr = str(obj.key)
    last_slash_index = dirStr.rfind('/')
    result = dirStr[:last_slash_index]
    if not os.path.exists(result):
        os.makedirs(result)
    # 下载Object到本地文件，并保存到指定的本地路径D:\\localpath\\examplefile.txt。如果指定的本地文件存在会覆盖，不存在则新建。
    # 这个东西必须要文件存在才可以下载
    bucket.get_object_to_file(obj.key, f'{obj.key}') 