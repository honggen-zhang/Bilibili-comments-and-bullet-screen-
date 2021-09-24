# Bilibili-comments-and-bullet-screen-
Extracting comments and bullet screen on Bilibili
## Scraping comments and bulletscreen given URL
**scrape.py** is used to extract commens and bullet screen from website. We can obtain two files: comments.csv and barrage.csv.
## Keyword extraction using jieba
We use jieba, a NLP tool, to do Chinese word segmentation. Runing the following code:
```bash
content = open(file_name(E.g. comments.csv), 'rb').read()
tags = jieba.analyse.extract_tags(content, topK=100)
```
