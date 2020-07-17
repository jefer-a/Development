import requests
import re

# 获取HTML
def getHtml(url):
    try:
        headersjson={'user-agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        response=requests.get(url,headers=headersjson)
        print(response.status_code)
        response.raise_for_status
        response.encoding=response.apparent_encoding
        return response
    except Exception as ex:
        print(ex)
        return ''

def htmlProcess():

    def out2Doc(pTags):
        with open('/python/spider/baiduwenku_out.doc','w',encoding='utf-8') as fo:
            line=''
            n=0
            for pTag in pTags:
                if pTag.string!="\n":
                    print(pTag.string)
                    n=0
                    ptxt=pTag.string
                    line+=ptxt.strip('\n\t ')
                else:
                    n+=1
                line+='\n\t' if n==1 else ''
            line=line.strip('\n')
            fo.write(line)

    def out2Txt(pTags):
        with open('/python/spider/baiduwenku_out.txt','w',encoding='utf-8') as fo:
            fo.writelines(line.string for line in pTags)
    
    with open('/python/spider/cache.txt','+r',encoding='utf-8') as fo:
        text=fo.read()
        from bs4 import BeautifulSoup as bs
        soup=bs(text,'html.parser')
        soup=bs(soup.prettify(),'html.parser')
        div=soup.find('div',attrs={'class':'ie-fix'})
        pTags=div.find_all('p','reader-word-layer')
        out2Txt(pTags)
        out2Doc(pTags)
        

def main(url):
    getHtml(url)
    htmlProcess()

if __name__ == '__main__':
    url='https://wenku.baidu.com/view/dbad263fbc64783e0912a21614791711cc797974.html'
    main(url)
    