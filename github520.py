import requests
import os
# 获取网络host 文件
url = 'https://raw.hellogithub.com/hosts'
response = requests.get(url)
host = response.text
print(host,type(host))

# 改写或者追加 系统host文件
hostfile = r'C:\Windows\System32\drivers\etc\hosts'
with open(hostfile,'r') as f:
    fd = f.readlines()
    new_host = []
    start = False
    # print(fd)
    for l in fd: ##删除旧的信息
        ret =  l.find('# GitHub520 Host Start')
        if ret != -1: #包含字符串则
            start = True

        if start == False:
            new_host.append(l)

        if l.find('# GitHub520 Host End') != -1:
            start = False

    new_host.append(host) #添加新的信息

with open(hostfile,'w') as f:#添加新的信息
    f.writelines(new_host)

# 刷新dns
ret = os.system('ipconfig /flushdns')
if ret == 0:
    print('执行成功')
else:
    print("执行失败")

while True:
    pass
