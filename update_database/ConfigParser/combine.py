#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

'''
 @Author      : Simon Chen
 @Email       : bafelem@gmail.com
 @datetime    : 2018-11-05 17:42:11
 @Description : Description
 @FileName    : combine.py
'''

import os
from configparser import ConfigParser

HOME = os.path.expanduser('~')

class Scanfolder:
    def __init__(self,folder_lev1, ca_us_lev2):
        self.folder_lev1 = folder_lev1
        self.folder_lev2 = ca_us_lev2
        self.folder_lev3 = []
        self.folder_lev4 = ['archive','running']
        self.job_folder = []
        self.folder_lev3_True = []

    def ls_lev3(self):
        for f2 in self.folder_lev2:
            f2path = os.path.join(self.folder_lev1,f2)
            if os.path.isdir(f2path):
                k = os.listdir(f2path)
                self.folder_lev3.extend(k)
        return self.folder_lev3

    def ls_lev4(self):
        for f2 in self.folder_lev2:
            f2 = os.path.join(self.folder_lev1,f2)
            for f3 in self.ls_lev3():
                f3 = os.path.join(f2,f3)
                for f4 in self.folder_lev4:
                    f4 = os.path.join(f3,f4)
                    if os.path.isdir(f4):
                        self.job_folder.append(os.listdir(f4))
                        self.folder_lev3_True.append(f4)

    def path_combine(self):
        self.ls_lev4()
        jobs_path = []
        length = len(self.folder_lev3_True)
        for a in range(length):
            for f in self.job_folder[a]:
                if f[0] == '.':
                    pass
                else:
                    jobs_path.append(self.folder_lev3_True[a]+'/'+f)
        return jobs_path

    def print_path(self):
        print(self.folder_lev1)
        print(self.folder_lev2)

class Scan_other_folder:
    def __init__(self,folder_lev1,other_lev2):
        self.folder_lev1 = folder_lev1
        self.folder_lev2 = other_lev2
        self.folder_lev3 = ['archive','running']
        self.job_folder = []
        self.folder_lev3_True = []

    def ls_lev4(self):
        for f2 in self.folder_lev2:
            f2 = os.path.join(self.folder_lev1,f2)
            for f3 in self.folder_lev3:
                f3 = os.path.join(f2,f3)
                if os.path.isdir(f3):
                    self.job_folder.append(os.listdir(f3))
                    self.folder_lev3_True.append(f3)

    def path_combine(self):
        self.ls_lev4()
        jobs_path = []
        length = len(self.folder_lev3_True)
        for a in range(length):
            for f in self.job_folder[a]:
                if f[0] == '.':
                    pass
                else:
                    jobs_path.append(self.folder_lev3_True[a]+'/'+f)
        return jobs_path

class Scan_LNC_folder:
    def __init__(self,folder_lev1):
        self.folder_lev1 = folder_lev1
        self.folder_lev2 = []
        self.folder_lev3 = ['archive','running']
        self.job_folder = []
        self.folder_lev3_True = []

    def ls_lev2(self):
        for f2 in os.listdir(self.folder_lev1):
            f2path = os.path.join(self.folder_lev1,f2)
            if os.path.isdir(f2path):
                self.folder_lev2.append(f2)
        return self.folder_lev2

    def ls_lev3(self):
        for f2 in self.ls_lev2():
            f2 = os.path.join(self.folder_lev1,f2)
            for f3 in self.folder_lev3:
                f3 = os.path.join(f2,f3)
                if os.path.isdir(f3):
                    self.job_folder.append(os.listdir(f3))
                    self.folder_lev3_True.append(f3)

    def path_combine(self):
        self.ls_lev3()
        jobs_path = []
        length = len(self.folder_lev3_True)
        for a in range(length):
            for f in self.job_folder[a]:
                if f[0] == '.':
                    pass
                else:
                    jobs_path.append(self.folder_lev3_True[a]+'/'+f)
        return jobs_path

def all_the_jobs():
    cfg = ConfigParser()
    cfg.read(HOME + '/Documents/GoGoConfig/config.ini')
    a = Scanfolder(cfg.get('us_ca','us_main'),cfg.get('us_ca','ca_us_lev2').split(','))
    b = Scanfolder(cfg.get('us_ca','ca_main'),cfg.get('us_ca','ca_us_lev2').split(','))
    c = Scan_other_folder(cfg.get('other','other_main'),cfg.get('other','other_lev2').split(','))
    d = Scan_LNC_folder(cfg.get('lnc','lnc_main'))
    all_jobs = []
    all_jobs.extend(a.path_combine())
    all_jobs.extend(b.path_combine())
    all_jobs.extend(c.path_combine())
    all_jobs.extend(d.path_combine())
    return all_jobs

def haha():
    print('haha')

if __name__ == "__main__":
    a=1
    for job in all_the_jobs():
        print(job,a)
        a=a+1



