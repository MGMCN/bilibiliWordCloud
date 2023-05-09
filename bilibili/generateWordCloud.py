from wordcloud import WordCloud
import jieba

stopwords = [
    "的", "了", "在", "是", "我", "你", "他", "她", "它", "们", "和", "与", "或", "而", "然", "但", "因", "所", "就",
    "那", "这", "一", "有", "无", "很", "非", "最", "更", "只", "不", "可", "能", "要", "想", "去", "来", "到", "从",
    "为",
    "对", "啊", "哦", "嗯", "嘿", "咦", "呀", "哇", "哈", "呜", "喔", "唉", "哎", "噢", "我们", "你们", "他们", "她们",
    "它们", "然而", "那么", "这样", "这个", "那个", "一些", "一种", "一样", "没有", "非常", "可以", "能够", "因为",
    "所以",
    "就是说", "例如", "比如", "不过", "然后", "接着", "现在", "一定", "一直", "仍然", "还是", "依然", "如何", "怎么",
    "怎样",
    "为什么", "由于", "尽管", "虽然", "很多", "许多", "某些", "每个", "全部", "整个", "部分", "其中", "其实", "实际上",
    "基本上",
    "总体上", "可能是", "可能会", "可能有", "不能", "不要", "不必", "不会", "不需要", "不应该", "应该",
    "必须", "一定要", "需要", "必须要"
]
comments = []

f = open('comments.txt')
line = f.readline()
while line:
    comments.append(line)
    line = f.readline()
f.close()

words = []
for comment in comments:
    # jieba.lcut(comment, cut_all=False, HMM=True)  # 精确模式
    # jieba.lcut(comment, cut_all=True, HMM=True)  # 全模式
    # jieba.lcut_for_search(comment, HMM=True)  # 搜索引擎模式
    cut_words = jieba.lcut(comment, cut_all=False, HMM=True)
    filtered_words = [word for word in cut_words if word not in stopwords]
    words.extend(filtered_words)

wc = WordCloud(
    font_path='./simhei.ttf',
    background_color="white",  # 背景颜色
    max_words=50,  # 词云显示的最大词数
    max_font_size=500,  # 字体最大值
    min_font_size=20,  # 字体最小值
    random_state=42,  # 随机数
    collocations=False,  # 避免重复单词
    width=1300, height=900, margin=10,  # 图像宽高，字间距，需要配合下面的plt.figure(dpi=xx)放缩才有效
)

temp = ' '.join(words)
wc.generate(temp)
wc.to_file('./output.jpg')
