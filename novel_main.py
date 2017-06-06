#!/usr/bin/python
# coding=UTF-8
import os
os.chdir('/projects/novel')
import novel
import sys
import time
sys.stdout = sys.stderr = open('/projects/novel/log', 'a+', 0)

books=[]
qidian_reg = '\{\"uuid.*?\"cN\":\"(.*?)\".*?\"id\":(.*?),.*?\}'
books.append(novel.lee_novel1('http://book.qidian.com/ajax/book/category?_csrfToken=&bookId=3638453', '五行天', qidian_reg, ''))
books.append(novel.lee_novel1('http://book.qidian.com/ajax/book/category?_csrfToken=&bookId=3489766', '全职法师', qidian_reg, ''))
while True:
    for book in books:
        book.process()    
    time.sleep(120)
