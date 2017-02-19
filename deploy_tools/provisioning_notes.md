# 配置新网站

## 需要安装的包

* nginx
* Python3
* Git
* pip
* virtualenv

以Ubuntu为例，可以执行下面的命令安装：

​	sudo apt-get install nginx git python3 python3-pip

​	sudo pip3 install virtualenv

##  配置Nginx虚拟主机

* 参考nginx.template.conf

* 把SITENAME替换成所需的域名，例如lists.my-domain.com

  其中static为静态文件目录

  proxy_set无需修改，proxy_pass采用了unix域套接字

## Upstart任务（Ubuntu15.04后为systemd）

* 参考gunicorn-systemctl.template.service
* 把SITENAME替换成所需的域名
* 放置在/lib/systemd/system/下，service文件写法可参考该目录下其他文件，若要设置开机启动需要enable该服务

## 文件夹结构

假设有用户账户，家目录为/home/username

/home/username

``` 
	└─ sites

		└─ SITENAME

			├  database

			├  source

			├  static

			└ virtualenv

```







