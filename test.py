# coding: utf-8

from selenium import webdriver
from bs4 import BeautifulSoup
import MySQLdb, re,json,time
from qiniu import Auth
from qiniu import BucketManager



from selenium import webdriver
from upload_qiniu import upload_qiniu


access_key = 'lO44qI2dlzLylW5clwp-KUD8ve9Z_UHpi-7zCsho'
secret_key = 'b2fJAuK9ACkEkpEcVpAk1DyTdQXhb6WDnB7h8pHT'
#初始化Auth状态
q = Auth(access_key, secret_key)
#初始化BucketManager
bucket = BucketManager(q)
#你要测试的空间， 并且这个key在你空间中存在
bucket_name = 'inst'


db = MySQLdb.connect(host='localhost', user='root', passwd='root', db='inst', charset='utf8')
cursor = db.cursor()
sql = "select id , qiniu_url from instagram where date like '%年%'"
cursor.execute(sql)
db.commit()
results =  cursor.fetchall()
for i in range(len(results)):
    res = results[i]
    key = res[1].split('http://ou43h7cjd.bkt.clouddn.com/')[1]
    ret, info = bucket.delete(bucket_name, key)
    print(info)
    sql1 = "delete from instagram where id = " + str(res[0])
    cursor.execute(sql1)
    db.commit()
     
    
    







