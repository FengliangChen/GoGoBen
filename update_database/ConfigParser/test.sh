#!/bin/sh

if ! [ -e /Volumes/datavolumn_bmkserver_Pub ]; then
	echo "检查服服器pub是否连接。"
	exit 0
elif ! [ -e /Volumes/datavolumn_bmkserver_Pub/新做稿/已结束/NON-WMT/.database ]; then
	mkdir /Volumes/datavolumn_bmkserver_Pub/新做稿/已结束/NON-WMT/.database && echo "已建文件夹于/Volumes/datavolumn_bmkserver_Pub/新做稿/已结束/NON-WMT/.database"
fi

if ! [ -e $HOME/Documents/.GoGoBen ];then
	mkdir $HOME/Documents/.GoGoBen && echo "已建隐藏文件夹Documents/.GoGoBen"
fi

if ! [ -e $HOME/Documents/GoGoConfig ];then
	mkdir $HOME/Documents/GoGoConfig && echo "已建文件夹Documents/GoGoConfig, 请放配置文件,再重新运行。"
	exit 0
fi

if ! [ -f $HOME/Documents/GoGoConfig/config.ini ];then
	echo "请确认文件夹Documents/GoGoConfig已有配置文件"
	exit 0
fi

if ! [ -f $HOME/Documents/GoGoConfig/database_storage/database_storage ];then
	echo "请确认已安装程序。"
	exit 0
fi


DB_FOLDER=$HOME/Documents/.GoGoBen
EXE_FOLDER=$HOME/Documents/GoGoConfig/database_storage

start_time=`date +%s`

cd ${EXE_FOLDER} && ./database_storage && cd ${DB_FOLDER} && cp search.db /Volumes/datavolumn_bmkserver_Pub/新做稿/已结束/NON-WMT/.database/search.db

echo "更新耗时$(expr `date +%s` - $start_time)秒。"
exit 0
