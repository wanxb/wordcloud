from wordcloud import WordCloud
import jieba
import numpy as np
from PIL import Image
import os

def read_file(file_path):
    with open(file_path, encoding='utf8') as file:
        return file.read()

def read_list_file(file_path):
    with open(file_path, encoding='utf8') as file:
        return file.read().split("\n")

# 文件路径
comments_file_path = "../data/data_contents.txt"
add_words_file_path = "../data/add_words.txt"
stopwords_file_path = "../data/stopwords.txt" 
font_path = '../fonts/simfang.ttf'
background_image_path = '../images/background_image.png'
width = 800
height = 800

# 读取数据
string_data = read_file(comments_file_path)

# 读取需要添加的词语
add_words_data = read_list_file(add_words_file_path)

# 添加组合词，不会被分割
for word in add_words_data:
    jieba.add_word(word)

# 分词
comment_text = jieba.cut(string_data)
text = ' '.join(comment_text)

# 读取停用词
stopwords_data = read_list_file(stopwords_file_path)

# 判断背景图片文件是否存在
bg = None
if os.path.exists(background_image_path):
    with Image.open(background_image_path) as bg_img:
        bg = np.array(bg_img)

# 创建WordCloud对象
wc = WordCloud(
    collocations=False,
    background_color='white',
    font_path=font_path,
    width=width,
    height=height, 
    stopwords=stopwords_data,
    mask=bg
)

# 生成词云
wc.generate(text)

# 保存图片
wc.to_file('word.png')