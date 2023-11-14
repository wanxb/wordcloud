# 词云生成器

这个项目使用Python生成词云图，通过分词、去除停用词和添加自定义词语来创建词云图。支持添加背景图片以及调整生成的词云图的样式。

![如图](images/word.png)

## 环境要求

- Python 3.8
- 依赖模块：`wordcloud`, `jieba`, `numpy`, `Pillow`

## 安装依赖

在项目根目录运行以下命令安装所需依赖：

```bash
	pip install wordcloud jieba numpy Pillow
```

## 项目结构

- data_contents.txt: 包含用于生成词云的文本数据的文件。
- add_words.txt: 包含需要添加到分词词典的自定义词语的文件。
- stopwords.txt: 包含停用词的文件。
- background_image.png: 用作词云背景的图片文件。
- wordcloud_generator.py: 生成词云的Python脚本。
- word.png: 生成的词云图像。

## 使用方法

- 在 data_contents.txt 中提供要生成词云的文本数据。
- 在 add_words.txt 中添加需要添加到分词词典的自定义词语，每行一个词。
- 在 stopwords.txt 中添加停用词，每行一个词。
- （可选）提供用作词云背景的 background_image.png。
- 运行 wordcloud_generator.py 脚本以生成词云图像。

``` python
	python wordcloud_generator.py
```
生成的词云图像将保存为 word.png。

## 注意事项

- 请确保已安装所需的Python版本和依赖。
- 自定义词语和停用词应适应你的数据和需求，可以根据需要进行调整。
- 如果没有提供背景图片，将不会添加背景。