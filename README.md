# bilibiliWordCloud
![image](https://img.shields.io/github/actions/workflow/status/MGMCN/bilibiliWordCloud/release.yml?label=build&logo=github)
![image](https://img.shields.io/docker/pulls/godmountain/bilibili-wordcloud)
![image](https://img.shields.io/github/last-commit/MGMCN/bilibiliWordCloud?logo=github)
![image](https://img.shields.io/github/license/MGMCN/bilibiliWordCloud)  

该程序实现了利用基于scrapy框架编写的爬虫程序爬取b站番剧短评，然后利用jieba库对爬取的短评分词，最后使用wordcloud展示的功能。( ps: 多年前写的代码，最近偶然整理文件夹时看到了，跑了一下居然还能用，觉得还挺有趣，就传上来了。)
## 使用指南
先确保你电脑安装了docker，以下docker的安装教程只针对MacOS用户。
```Bash
$ brew install --cask docker # 确保你已经安装了brew 
```
运行docker，你也可以直接在你应用里找到Docker.app然后双击运行启动。
```Bash
$ open /Applications/Docker.app
```
如果你想直接拉取我们编译好的镜像并运行，你需要确认你的操作系统架构基于以下两种。
> linux/arm64  
> linux/amd64
### 拉取镜像运行
```Bash
$ docker pull godmountain/bilibili-wordcloud:latest
$ docker run --name bilibili -e media_id=1586 godmountain/bilibili-wordcloud:latest # media_id参数指定了爬取番剧
.
.
.
$ docker cp bilibili:/proj/bilibili/output.jpg /your/local/path # 别忘记了修改后面这个路径
```
当你在本地打开output.jpg后你就能看到  

<img src="https://github.com/MGMCN/bilibiliWordCloud/blob/main/bilibili/output.jpg" width = "435" height = "300"/>  

media_id的含义请参照 -> [如何找到对应番剧的media_id](#mediaid)
## 怎样在本地构建你自己的docker镜像
进入Dockerfile所在目录，然后使用build指令构建你自己的镜像。
```Bash
$ ls # 先确保你在的目录下有Dockerfile文件
.
├── Dockerfile
├── LICENSE
├── README.md
├── bilibili
├── images
└── requirements.txt
$ docker build . bilibili
$ docker run --name bilibili -e media_id=1586 bilibili
```
等待程序执行结束后将wordcloud生成的图片拷贝到本地查看
```Bash
$ docker cp bilibili:/proj/bilibili/output.jpg /your/local/path # 别忘记了修改后面这个路径
```

## <a name="mediaid">怎样修改爬取的番剧</a>

打开你的b站找到一部你想爬取的番剧或者电影，只要有短评这个选项的都能爬。( ps: 请注意是短评不是评论🤪. ) 然后点击下面图示中的查看全部选项。   

<img src="./images/page.png" width = "1140" height = "500"/>  

复制打开页面的链接中md后面的那串数字，在这个例子中是'1586'

<img src="./images/link.png" width = "790" height = "66"/>  





