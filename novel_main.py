#!/usr/bin/python
# coding=UTF-8
import os
os.chdir('/projects/novel')
import novel
import sys
import time
sys.stdout = sys.stderr = open('/projects/novel/log', 'a+', 0)

books=[]
#books.append(novel.lee_novel('http://www.qianrenge.com/book/61/61452/', '五行天', '<dd> <a style="" href="([\s\S]+?)">([\s\S]+?)</a></dd>', '<div id="content">([\s\S]+?)</div>'))
#books.append(novel.lee_novel('http://www.qianrenge.com/book/27/27356/','全职法师', '<dd> <a style="" href="([\s\S]+?)">([\s\S]+?)</a></dd>', '<div id="content">([\s\S]+?)</div>'))
books.append(novel.lee_novel1('http://read.qidian.com/BookReader/82plFx6pHLY1.aspx', '五行天', '<li style=\'width:33%;\'><a[\s\S]*?href="([\s\S]+?)"[\s\S]*?target=\'_blank\'>([\s\S]+?)</a></li>', ''))
books.append(novel.lee_novel1('http://read.qidian.com/BookReader/NxlTJG8OMTs1.aspx', '全职法师', '<li style=\'width:33%;\'><a[\s\S]*?href="([\s\S]+?)"[\s\S]*?target=\'_blank\'>([\s\S]+?)</a></li>', ''))
while True:
    for book in books:
        book.process()    
    time.sleep(120)
