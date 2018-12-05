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

print('数据库更新中。。。')
HOME = os.path.expanduser('~')
sqlite_file = HOME + '/Documents/build/new_scan/search.db'    # name of the sqlite database file

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

all_jobs = sort_job.sort_job()

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
a=0
while True:
	try:
		insert_job(all_jobs[0][a],all_jobs[1][a])
	except IndexError:
		print("数据库更新完成。")
        print("共收集{}个单号".format(a))
		break
	a = a + 1

conn.commit()
conn.close()
exit()
# if __name__ == "__main__":