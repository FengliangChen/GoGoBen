#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

'''
 @Author      : Simon Chen
 @Email       : bafelem@gmail.com
 @datetime    : 2018-11-06 22:05:40
 @Description : Description
 @FileName    : client.py
'''

import os
import datetime
import re
import subprocess
import sqlite3
import tkinter as tk
import tkinter.messagebox

HOME = os.path.expanduser('~')
path1 = '/Volumes/datavolumn_bmkserver_Pub/新做稿/已结束/NON-WMT/.database/search.db'
path2 = HOME+'/Documents/.GoGoBen/search.db'
path3 = "/Volumes/datavolumn_bmkserver_Design/WMT-USA"
log_path = HOME+'/Documents/.GoGoBen/log'

wks_path = "/Volumes/datavolumn_bmkserver_Pub/新做稿/未开始"
jxz_path = "/Volumes/datavolumn_bmkserver_Pub/新做稿/进行中"


def check_server():
    ist1 = os.path.exists(path1)
    ist2 = os.path.exists(path2)
    ist3 = os.path.exists(path3)
    if not ist1:
        tk.messagebox.showinfo(title="注意", message= '请检查服务器pub是否已连接。')
    if not ist2:
    	subprocess.call(["cp", path1, path2])
    if not ist3:
        tk.messagebox.showwarning(title="警告", message= '请检查服务器design是否已连接。')
        exit()

def compare_db_time():
    try:
        with open(log_path,'r') as f:
            f = str(f.read())
            file1_mtime = os.path.getmtime(path1)
            if f != str(file1_mtime):
                subprocess.call(['cp', path1, path2])
                ct1 = datetime.datetime.fromtimestamp(file1_mtime)
                with open(log_path,'w') as f:
                    file1_mtime = os.path.getmtime(path1)
                    f.write(str(file1_mtime))
                return "采集于{}".format(ct1)
    except FileNotFoundError:
        with open(log_path,'w') as f:
            file1_mtime = os.path.getmtime(path1)
            f.write(str(file1_mtime))

def search_database(pattern,sqlite_file):
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute("SELECT job_number, file_path FROM First_test WHERE job_number LIKE (?)",('%'+pattern+'%',))
    value = c.fetchall()
    conn.close()
    return value

def draft_search(pattern):
    for folder in [wks_path, jxz_path]:
        for file in os.listdir(folder):
            m=re.search(pattern, file)
            if m:
                if m[0] != '.': 
                    return os.path.join(folder,file)

def check_digit():
    k = entry_text.get()
    k = k.upper()
    if len(k) == 6:
        return k
    if len(k) == 4:
        result = draft_search(k)
        if result:
            subprocess.call(["open", draft_search(k)])
        else:
            tk.messagebox.showwarning(title="找不到", message= '我怎么都找不到，你自己打开吧。')
    else:
        tk.messagebox.showwarning(title="输入错误", message= '请输入四或六位数')
        return False

def go(event=None):
    check_server()
    db_time_result = compare_db_time()
    if db_time_result:
        label_text.set(db_time_result)
    k = check_digit()
    if k:
        path = search_database(str(k),path2)
        if path:
            subprocess.call(["open", path[0][1]])
        else:
            tk.messagebox.showwarning(title="找不到", message= '我怎么都找不到，你自己打开吧。')

def about_gogoben():
    tk.messagebox.showinfo(title="关于GoGoBen", message= 'GoGoBen由Simon Chen 开发及维护。\n      联系：bafelem@gmail.com \n\n\n       GoGoBen version 1.0.1')

def help_gogoben():
    tk.messagebox.showinfo(title="帮助", message='输入单号的六位打开design文件夹，输入单号的后四位（即省去年份）可打开“新做稿“或”进行中“的文件夹。')
       
def run():
    root = tk.Tk()
    root.title('Go Go Ben')
    root.resizable(0,0)
    menu_bar = tk.Menu(root)
    about_menu = tk.Menu(menu_bar, tearoff=0)
    about_menu.add_command(label='关于 GoGoBen', command = about_gogoben)
    about_menu.add_command(label='帮助', command = help_gogoben)
    menu_bar.add_cascade(label='关于', menu=about_menu)
    root.config(menu=menu_bar)
    global label_text
    global entry_text
    label_text = tk.StringVar()
    entry_text = tk.StringVar()
    tk.Label(root, text ="   Job:" ).grid(row = 0, column=0, sticky = 'w')
    tk.Label(root,textvariable = label_text, width = 20, foreground="steelblue").grid(row = 1, column=1, sticky = 'w')
    tk.Label(root).grid(row = 1, column=0,sticky = 'w')
    entry = tk.Entry(root, width=20, textvariable = entry_text)
    entry.focus()
    entry.grid(row = 0, column=1, sticky = 'w')
    tk.Button(root, text="Quit", command = root.quit).grid(row=2, column=0, sticky='w')
    tk.Button(root, text="Go", command = go).grid(row=2, column=1, sticky='e')
    root.bind("<Return>", go)
    root.bind("<KP_Enter>", go)
    root.mainloop()


if __name__ == "__main__":
    run()