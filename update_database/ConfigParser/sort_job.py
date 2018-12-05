#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

'''
 @Author      : Simon Chen
 @Email       : bafelem@gmail.com
 @datetime    : 2018-10-26 14:37:42
 @Description : Description
 @FileName    : storage.py
'''

import os
import re
import combine

# with open("/Users/imac-6/Desktop/canada_case.txt",'r') as f:
#     f = f.read()

def job_fetch(file):
    pattern='[BCPTU][\d]{4}[0-9A-Z]{2}[_][A-Z]{3}'
    m=re.search(pattern, file)
    if m:
        return m.group(0)

def sort_job():
    jobs=[]
    pathes=[]
    for lines in combine.all_the_jobs():
        if job_fetch(lines):
            jobs.append(job_fetch(lines))
            pathes.append(lines)
    return (jobs,pathes)



def test():
    print(sort_job())

if __name__ == "__main__": test()