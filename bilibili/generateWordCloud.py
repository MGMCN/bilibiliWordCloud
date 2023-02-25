from wordcloud import WordCloud
import jieba

comments = []

f = open('comments.txt')
line = f.readline()
while line:
    comments.append(line)
    line = f.readline()
f.close()


words = []
for comment in comments:
    words.extend(jieba.lcut(comment, cut_all=False, HMM=True))  # 精确模式
    # words.extend(jieba.lcut(comment, cut_all=True, HMM=True))  # 全模式
    # words.extend(jieba.lcut_for_search(comment, HMM=True))  # 搜索引擎模式

wc = WordCloud(
    font_path='./simhei.ttf',
    background_color="white",  # 背景颜色
    max_words=100,  # 词云显示的最大词数
    max_font_size=500,  # 字体最大值
    min_font_size=20,  # 字体最小值
    random_state=42,  # 随机数
    collocations=False,  # 避免重复单词
    width=1300, height=900, margin=10,  # 图像宽高，字间距，需要配合下面的plt.figure(dpi=xx)放缩才有效
)

temp = ' '.join(words)
wc.generate(temp)
wc.to_file('./output.jpg')
