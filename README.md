# 考研院校推荐
根据学生查看的专业为学生推荐相关的学校信息

## 环境配置
安装anaconda;

命令行输入conda create -n web python=3.6;

打开代码，找到conn.py,修改数据库信息;

pycharm右下角点击<No interpreter>,点击add python interpreter;
  
选择conda environment，点击interpreter，选择anaconda\envs\web\python.exe;
  
在代码目录打开终端，输入pip install falsk -i https://pypi.tuna.tsinghua.edu.cn/simple some-package;
  
接着输入pip install pandas -i https://pypi.tuna.tsinghua.edu.cn/simple some-package;
  
接着输入pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple some-package;
  
接着输入pip install beautifulsoup4 -i https://pypi.tuna.tsinghua.edu.cn/simple some-package;
  
配置完成后运行api.py,在相应的本地端口打开即可
