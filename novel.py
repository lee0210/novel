# coding=UTF-8
import urllib2
import time
import re
import os
import db

class lee_novel():

    def __init__(self, book_url, book_name, check_update_pattern, get_content_pattern):
        self.book_url, self.book_name, self.check_update_pattern, self.get_content_pattern = book_url, book_name, check_update_pattern, get_content_pattern
        #self.r = redis.StrictRedis(host='b.leezypig.com', db=1)
        novel =db.novel.get()
        novel.name = self.book_name
        novel._key_list = ['name']
        self.urls = []
        for n in novel:
            self.urls.append(n.url)

    def check_update(self, pattern):
    # return an iterator for update url list
        print 'checking update ' + self.book_name
        r = urllib2.urlopen(self.book_url)
        html = r.read()
        encoding = self.get_encoding(html)
        for url, title in reversed(re.findall(pattern, html)):
           url = self.book_url + url
           if url not in self.urls:
               yield url, title.decode(encoding, 'ignore').encode('utf-8')

    def process(self):
        try:
            for url, title in self.check_update(self.check_update_pattern):
                content = self.get_content(url, self.get_content_pattern)
                file_path = './books/%s/'%(self.book_name)
                if not os.path.exists(file_path):
                    os.mkdir(file_path)
                file_path += title
                f = open(file_path, 'wb')
                f.write('Subject: %s %s\n'%(self.book_name, title))
                f.write('Content-Type: text/html; charset=UTF-8;\n')
                f.write(content)
                f.close()
                print 'Saved to %s.'%(file_path)
                os.system("cat '%s' | sendmail jw@qubitlee.com"%(file_path))
                #os.system("cat '%s' | sendmail lee0210@outlook.com"%(file_path))
                #self.r.sadd(self.book_name, url)
        except Exception, e:
            print time.ctime(), e

    def get_content(self, url, pattern):
    #return title and the content, both are UTF-8
        r = urllib2.urlopen(url)
        html = r.read()
        encoding = self.get_encoding(html)
        contents = re.findall(pattern, html)
        if len(contents) == 0 :
            raise Exception('Get content failed')
        return '<div>%s</div>' % ( contents[0].decode(encoding, 'ignore').encode('utf-8') )
    def get_encoding(self, html):
    #return the encoding of the html
        return re.findall('<meta .+?charset=(.+?)[\'\"].*?>', html)[0]

class lee_novel1(lee_novel):
    def process(self):
        novel = db.novel.get()
        print 'processing ' + self.book_name;
        try:
            for url, title in self.check_update(self.check_update_pattern):
                os.system('echo "There is an update available, please check." | mailx -s "%s %s" jw@qubitlee.com'%(self.book_name, title))
                novel.url = url
                novel.title = title
                novel.name = self.book_name
                novel.write()
                self.urls.append(url)
                print 'send mail for %s %s'%(self.book_name, title)
        except Exception, e:
            print time.ctime(), e



