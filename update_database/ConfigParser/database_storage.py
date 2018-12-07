#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

'''
 @Author      : Simon Chen
 @Email       : bafelem@gmail.com
 @datetime    : 2018-10-26 16:42:30
 @Description : Description
 @FileName    : database_storage.py
'''
import os
import sqlite3
import sort_job
import sys
from configparser import ConfigParser


HOME = os.path.expanduser('~')
cfg = ConfigParser()
cfg.read(HOME + '/Documents/GoGoConfig/config.ini')
sqlite_file = HOME + cfg.get('db_path','db')    # name of the sqlite database file

print('数据库更新中')

class SimpleProgressBar():
    def __init__(self, width=50):
        self.last_x = -1
        self.width = width

    def update(self, x):
        assert 0 <= x <= 100 # `x`: progress in percent ( between 0 and 100)
        if self.last_x == int(x): return
        self.last_x = int(x)
        pointer = int(self.width * (x / 100.0))
        sys.stdout.write( '\r%d%% [%s]' % (int(x), '#' * pointer + '.' * (self.width - pointer)))
        sys.stdout.flush()
        if x == 100: print('完成')

pd = SimpleProgressBar()
pd.update(0)

def creat_table():
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute('CREATE TABLE First_test (job_number TEXT, file_path TEXT)')
    conn.commit()
    conn.close()

def insert_job(jobs,pathes):
    with conn:
        c.execute("INSERT INTO First_test VALUES (?,? )", (jobs,pathes))

if os.path.exists(sqlite_file):
    os.remove(sqlite_file)

creat_table()
pd.update(10)

all_jobs = sort_job.sort_job()
pd.update(50)

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
a=0
while True:
    try:
        insert_job(all_jobs[0][a],all_jobs[1][a])
        if a == 1000:
            pd.update(70)
        if a == 2000:
            pd.update(90)
    except IndexError:
        pd.update(100)
        print("共收集{}个单号".format(a))
        break
    a = a + 1

conn.commit()
conn.close()

sys.exit()
# if __name__ == "__main__":