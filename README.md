# Thunneycomb 

# 2019-09-26 update  
1. 更新Django到2.x， 更新Python到3.5+
2. 删除非核心APP，只保留home、wiki、platycodon
3. 更新wiki版本



---------
Old update info
2016/07/02
# Merge wintercome to thunneycomb master.
# switch to thunneycomb product env.

2018/12/05
# UWSGI 需要系统支持，建议从源码安装：
- 安装说明：https://www.thunneycomb.com/wiki/learning_notes/setup_uwsgi/

2018/12/06
# mysqlclient支持 Debian / Ubuntu
- 官网说明：https://pypi.org/project/mysqlclient/
```bash
sudo apt-get install python3-dev default-libmysqlclient-dev
```

    

# Start server
```bash
uwsgi -i uwsgi.ini 
sudo /etc/init.d/nginx restart
```

