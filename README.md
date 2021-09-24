# Bilibili-comments-and-bullet-screen-
Extracting comments and bullet screen on Bilibili
## Scraping comments and bulletscreen given URL
**scrape.py** is used to extract commens and bullet screen from website. We can obtain two files: comments.csv and barrage.csv.
## Keyword extraction using jieba
We use jieba, a NLP tool, to do Chinese word segmentation. Runing the following code:
```bash
content = open(file_name(E.g. comments.csv), 'rb').read()
top_words = jieba.analyse.extract_tags(content, topK=100)
```
Then, the **top_words** consist of topK words or phrase.
For example, the top10 words form website URL = https://www.bilibili.com/video/BV1W441127UG?from=search&seid=16535747710683710824&spm_id_from=333.337.0.0
| comment top10 keywords | bullet screen top10 keywords |
| ------- | ------ | 
| 啊啊啊   | 哈哈哈  | 
| 好听   | 哈哈哈哈  | 
| 春晚   | 蹦迪 | 
| 大哭   | 可爱  | 
| 喜欢   | 琵琶  | 
| 太棒了   | 小姐姐  | 
| 尺八   | 哈哈  | 
| 真的   | 画风  | 
| 视频   | 放飞 | 
| 琵琶   | 假酒  | 


