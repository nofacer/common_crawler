'''
Coded by Dustni
ｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｏｏｉｉｉｉｉ
ｉｉｏｏｏｏｏｏｏｏｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｏｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｏｏｉｉｉｉｉ
ｉｉｉｏｏｉｉｏｏｏｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｏｏｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉ
ｉｉｉｏｏｉｉｉｏｏｏｉｉｉｉｏｏｉｏｏｉｉｉｉｉｉｉｉｉｏｏｏｉｉｉｉｉｉｉｉｉｏｏｏｏｉｉｉｉｉｉｏｏｏｏｏｉｉｉｉｉｉｉｉｉｏｏｉｉｉｉｉ
ｉｉｉｏｏｉｉｉｉｏｏｉｉｉｉｉｏｉｉｏｉｉｉｉｉｉｉｉｏｏｏｏｉｉｉｉｉｉｉｉｉｉｏｉｉｉｉｉｉｉｉｉｏｏｏｏｉｉｉｉｉｉｉｉｉｏｏｉｉｉｉｉ
ｉｉｉｏｏｉｉｉｉｏｏｉｉｉｉｉｏｉｉｏｉｉｉｉｉｉｉｉｉｏｏｏｉｉｉｉｉｉｉｉｉｉｏｉｉｉｉｉｉｉｉｉｏｉｉｏｉｉｉｉｉｉｉｉｉｏｏｉｉｉｉｉ
ｉｉｉｏｏｉｉｉｏｏｏｉｉｉｉｉｏｏｏｏｉｉｉｉｉｉｉｉｉｏｏｏｏｉｉｉｉｉｉｉｉｉｏｉｉｉｉｉｉｉｉｉｏｉｉｏｉｉｉｉｉｉｉｉｉｏｏｉｉｉｉｉ
ｉｉｉｏｏｏｏｏｏｏｉｉｉｉｉｉｏｏｏｏｏｉｉｉｉｉｉｉｉｏｏｏｏｉｉｉｉｉｉｉｉｉｏｏｏｉｉｉｉｉｉｏｏｏｏｏｏｉｉｉｉｉｉｉｉｏｏｏｉｉｉｉ
ｉｉｏｏｏｏｏｏｏｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｏｏｏｉｉｉｉｉｉｉｉｉｉｏｏｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉ
ｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉ
ｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉ
ｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉｉ

Usage 


crawler=Crawler(['http://www.tongliao.gov.cn/'],'data.db',2)
crawler.create_database()
crawler.crawl()

se=Searcher('data.db',['你好','hello'])
print(se.search())

'''
import urllib.request as ur
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from sqlite3 import dbapi2 as sqlite
import re

class Crawler:
    def __init__(self,target_index,db_name,depth):
        self.target_index=target_index

        self.depth=depth
        self.result=[]

        self.con=sqlite.connect(db_name)

    def create_database(self):
        try:
            self.con.execute('create table urls(url,content)')
            self.con.commit()
        except:
            print('There is error when create table')

    def is_indexed(self,url):
        u=self.con.execute("select rowid from urls where url='%s'" % url ).fetchone()
        if u!=None:
            return True
        else:
            return False

    def get_text(self,soup):
        v=soup.string
        if v==None:
            c=soup.contents
            resulttext=''
            for t in c :
                subtext=self.get_text(t)
                resulttext+=subtext+'\n'
            return resulttext
        else:
            return v.strip()

    def separate(self,text):
        splitter=re.compile('\\W*')
        return [s.lower() for s in splitter.split(text) if s!=' ']


    def add_to_index(self,url,soup):
        if self.is_indexed(url):return
        print('Indexing %s' % url)

        text=self.get_text(soup)
        words=self.separate(text)
        joined=''.join(words)
        print(joined)
        self.con.execute("insert into urls(url,content) values ('%s','%s')" % (url,joined))
        self.con.commit()



    def storage_file(self,file_name):
        pass

    def crawl(self):
        pages=self.target_index

        depth=self.depth

        for i in range(depth):
            newpages=[]
            for page in pages :
                try:
                    c=ur.urlopen(page)
                    print('Opening %s' % page)
                except:
                    print("Can't open %s" % page)
                    continue
                soup=BeautifulSoup(c.read(),"lxml")

                self.add_to_index(page,soup)


                links=soup('a')
                for link in links:
                    if('href' in dict(link.attrs)):
                        url=urljoin(page,link['href'])
                        if url.find("'")!=-1:
                            continue
                        url=url.split('#')[0]
                        if url[0:4]=='http' and  not self.is_indexed(url):
                            newpages.append(url)
            pages=newpages




class Searcher:
    def __init__(self,db,targets):
        self.db=db
        self.targets=targets
        self.con=sqlite.connect(db)
        self.result=[]

    def search(self):
        for target in self.targets:
            print(target)
            urlrow=self.con.execute("select url from urls where content like '%"+target+"%'" ).fetchall()

            if urlrow!=None:

                self.result.append(urlrow)
        return self.result







