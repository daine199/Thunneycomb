# wintercome
# Working on Py3.4 env.

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
uwsgi -i uwsgi_py34.ini 
sudo /etc/init.d/nginx restart
```

