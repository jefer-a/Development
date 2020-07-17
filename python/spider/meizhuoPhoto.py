import requests
import re
import time
import bs4
import os,sys
from bs4 import BeautifulSoup

count=0

def floder_dir(path):
    path_model=os.getcwd()+'\\photo\\'
    if not os.path.exists(path_model):
        os.mkdir(path_model)
    path=path_model+path
    if not os.path.exists(path):
        os.mkdir(path)
    return path+'\\'

def getHtml(url,flage=0):
    headersjson={'user-agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    r=requests.get(url,headers=headersjson)
    print('status:',r.status_code)
    img_src=[]
    img_href=[]
    try:
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        soup=BeautifulSoup(r.text,'html.parser')
        if flage==1:
            div=soup.find('div','pages')
            atage=div.find_all(string=re.compile(r'\d+'))
            return eval(atage[-1])
        elif flage==2:
            for li in soup.find_all('ul','clearfix')[1].children:
                time.sleep(0.2)
                if isinstance(li,bs4.element.Tag):
                    try:
                        href=li.find('a').attrs['href']
                        if href:
                            if 'http://www.win4000.com/' in href:
                                img_href.append(href)
                            else:
                                img_href.append('http://www.win4000.com'+href)
                    except :
                        continue
            return img_href
        else:
            img=soup.find('img','pic-large')
            if isinstance(img,bs4.element.Tag):
                try:
                    img_src=img.attrs['data-original']
                except :
                    try:
                        img_src=img.attrs['src']
                    except :
                        pass
            return img_src
    except :
        pass

def getPhoto(img_src,path):
    headersjson={'user-agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    global count
    for url in img_src:
        count+=1
        time.sleep(0.5)
        photo=url.split('/')[-1]
        img=requests.get(url,headers=headersjson)
        print(count,'status:',img.status_code)
        try:
            img.raise_for_status()
            with open(path+photo,"wb") as fo:
                fo.write(img.content)
        except :
            continue
def main(urls):
    for url in urls:
        size=getHtml(url,1)
        dir_file=url.split('.html')[0].split('_')[0]
        dir_file=dir_file.split('/')[-1]
        path=floder_dir(dir_file)
        print(path)
        url=url.split('.html')[0]+'_'
        for i in range(0,size,1):
            arg_url1=url+str(i+1)+'.html'
            img_href=getHtml(arg_url1,2)
            print('href获取完成:',str(i+1)+'/'+str(size))
            img_src=[]
            for arg_url2 in img_href:
                img_src.append(getHtml(arg_url2))
            print('src获取完成:',str(i+1)+'/'+str(size))
            getPhoto(img_src,path)

if __name__ == '__main__':
    urls={
        # 'http://www.win4000.com/mt/dengziqi.html',
        # 'http://www.win4000.com/sjzt/xingganmeinv.html',
        'http://www.win4000.com/wallpaper_2285_0_10.html'
    }
    main(urls)