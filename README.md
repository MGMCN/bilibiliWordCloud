# bilibiliWordCloud
该程序实现了利用基于scrapy框架编写的爬虫程序爬取b站番剧短评，然后利用jieba库对爬取的短评分词，最后使用wordcloud展示的功能。( ps: 多年前写的代码，最近偶然整理文件夹时看到了，跑了一下居然还能用，觉得还挺有趣，就传上来了。)
## 怎么运行这个代码
先确保你电脑安装了docker，并且能使用docker-compose指令。以下docker的安装教程只针对MacOS用户。
```Bash
$ brew install --cask docker # 确保你已经安装了brew 
```
运行docker，你也可以直接在你应用里找到Docker.app然后双击运行启动。
```Bash
$ open /Applications/Docker.app
```
在docker容器中运行我们的代码
```Bash
$ ls # 先确保你在的目录下有docker-compose.yml文件
.
├── Dockerfile
├── LICENSE
├── README.md
├── bilibili
├── docker-compose.yml
├── images
└── requirements.txt
$ docker compose up --build # 执行这个指令
```
等待程序执行结束后将wordcloud生成的图片拷贝到本地查看
```Bash
$ docker cp bilibili:/proj/bilibili/output.jpg /your/local/path # 别忘记了修改后面这个路径
```
当你在本地打开output.jpg后你就能看到  

<img src="https://github.com/MGMCN/bilibiliWordCloud/blob/main/bilibili/output.jpg" width = "435" height = "300"/>  

## 怎么修改这个代码爬取的番剧
打开你的b站找到你部你想爬取的番剧或者电影，只要有短评这个选项的都能爬。( ps: 注意是短评不是评论🤪. ) 点击查看全部。   

<img src="./images/page.png" width = "1145" height = "500"/>  

复制打开页面的链接里md后面的那串数字，在这个例子中是'1586'

<img src="./images/link.png" width = "790" height = "66"/>  

然后在我们的工程里找到下面这个文件
```Bash
$ ls
.
├── Dockerfile
├── LICENSE
├── README.md
├── bilibili
│   ├── bilibili
│   │   ├── __init__.py
│   │   ├── items.py
│   │   ├── middlewares.py
│   │   ├── pipelines.py
│   │   ├── settings.py
│   │   └── spiders
│   │       ├── __init__.py
│   │       └── bilibilicomment.py # 👈🏻打开这个文件
.
.
.
```
编辑下面media_id的参数
```Python
params = {
  'media_id': '1586', # 👈替换这个id为你拷贝的md后面那串数字
  'ps': '20',
  'sort': '0',
}
```
然后再次执行docker-compose指令( ps: 请确保你的docker已经启动。 )
```Bash
$ docker compose up --build # 回到docker-compose.yml所在目录。
.
.
.
$ docker cp bilibili:/proj/bilibili/output.jpg /your/local/path # 待运行结束后执行这个指令
```
## 如果你想在本地直接运行这个代码而不是在docker里运行
```Bash
$ ls # 先回到这个目录下
.
├── Dockerfile
├── LICENSE
├── README.md
├── bilibili
├── docker-compose.yml
├── images
└── requirements.txt
$ sudo pip3 install -r requirements.txt
$ cd bilibili
$ chmod +x run.sh
$ ./run.sh
.
.
.
$ open output.jpg # 因为是在本地运行的代码，生成的图片就直接输出在本地当前目录下了
```




