## 1.环境准备。  
### 安装相应模块和包:bs4,requests,csv,selenium。
## 2.爬取国家新闻出版署网络游戏审批信息，两种方法。
### 2.1 运行游戏版号爬取.py。
### 2.2 直接使用excel获取数据。
![excel1.png](image/excel1.png)
### 输入网址
![excel2.png](image/excel2.png)
### 选择加载获取全部内容或者选择数据转换进行筛选。
![excel3.png](image/excel3.png)
## 3.通过selenium模拟浏览器点击来获取taptap上的内容。
### 3.1 下载谷歌浏览器chrome。
### 3.2 将taptap数据爬取.py内的chrome_driver_path = "C:/Program Files/Google/Chrome/Application/chromedriver.exe"里的浏览器驱动路径替换成你的
### 3.3 运行taptap数据爬取.py。

## 4.注意事项，taptap数据爬取.py内只有爬取游戏标签的功能，如果需要爬取其他内容，希望能够自主学习并添加。