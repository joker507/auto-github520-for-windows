# 一个基于python更改hosts文件的程序-让你爱上github

> 参考：[521xueweihan/GitHub520: 让你“爱”上 GitHub，解决访问时图裂、加载慢的问题。（无需安装）](https://github.com/521xueweihan/GitHub520)

* 让程序帮你做下面的事情吧

1. 点击连接 https://raw.hellogithub.com/hosts
2. 全选复制内容
3. 打开 c:/windows/system32/drivers/etc/hosts
4. 在后面加入(原本有的话就替换)刚刚复制的内容
5.点击win健 输入cmd ,打开终端 输入 ipconfig /flushdns
6. 刷新github网站即可，有可能不行，看运气

* requirement

  `pip install request`



* 如果你需要打包成exe程序

  `pip install pyinstaller`



* 直接下载exe文件 ，双击运行
