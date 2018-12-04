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

class Scanfolder:
    def __init__(self,folder_lev1):
        self.folder_lev1 = folder_lev1
        self.folder_lev2 = ['2018', '2019']
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

class Scan_other_folder:
    def __init__(self,folder_lev1):
        self.folder_lev1 = folder_lev1
        self.folder_lev2 = ['BMT','CAB_2018','Other supplier','WKL']
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
    a = Scanfolder('/Volumes/datavolumn_bmkserver_Design/WMT-USA')
    b = Scanfolder('/Volumes/datavolumn_bmkserver_Design/WMT-Canada')
    c = Scan_other_folder('/Volumes/datavolumn_bmkserver_Design/Other')
    d = Scan_LNC_folder('/Volumes/datavolumn_bmkserver_Design/Other/LNC')
    all_jobs = []
    all_jobs.extend(a.path_combine())
    all_jobs.extend(b.path_combine())
    all_jobs.extend(c.path_combine())
    all_jobs.extend(d.path_combine())
    return all_jobs
    # print(a.path_combine(),b.path_combine(),c.path_combine(),d.path_combine())
    # print(all_jobs,len(all_jobs))

def haha():
    print('haha')
        
if __name__ == "__main__":
    print(all_the_jobs())



