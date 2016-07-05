# coding=UTF-8
import os
os.chdir('/projects/novel')
import novel
import sys
import time
sys.stdout = sys.stderr = open('/projects/novel/log', 'a+', 0)

books=[]
books.append(novel.lee_novel('http://www.qianrenge.com/book/61/61452/', '五行天', '<dd> <a style="" href="([\s\S]+?)">([\s\S]+?)</a></dd>', '<div id="content">([\s\S]+?)</div>'))
books.append(novel.lee_novel('http://www.qianrenge.com/book/27/27356/','全职法师', '<dd> <a style="" href="([\s\S]+?)">([\s\S]+?)</a></dd>', '<div id="content">([\s\S]+?)</div>'))
while True:
    for book in books:
        book.process()    
    time.sleep(120)
