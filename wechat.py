import urllib.request
import re
import urllib.error
import time
header=("User-Agent","Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36")
opener=urllib.request.build_opener()
opener.addheaders=[header]
urllib.request.install_opener(opener)
def proxy(proxy_addr,url): #使用代理来爬取内容
    try:
        proxy=urllib.request.ProxyHandler({'http':proxy_addr})
        opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
        urllib.request.install_opener(opener)
        data=urllib.request.urlopen(url).read()
        return data
    except urllib.error.URLError as e:
        if hasattr(e,'code'):
            print(e.code)
        if hasattr(e,'reason'):
            print(e.reason)
        time.sleep(3)
    except Exception as e:
        time.sleep(1)
def urlcontent(proxy_addr,page): #读取总的网址内容
        url="http://weixin.sogou.com/weixin?query=%E6%AF%94%E7%89%B9%E5%B8%81&_sug_type_=&sut=1315&lkt=1%2C1517969295463%2C1517969295463&s_from=input&_sug_=y&type=2&sst0=1517969295567&page=2&ie=utf8&w=01019900&dr=1"
        data=urllib.request.urlopen(url).read().decode("utf-8")
        urlpat='<a target="_blank" href="(http://mp.weixin.qq.com/s.*?amp;new=1)"'
        urlcollection=re.compile(urlpat).findall(data,re.S)
        return urlcollection
def getcontent(proxy_addr,page):
    html1="""<!DOCTYPE html>
<!--headTrap<body></body><head></head><html></html>--><html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <title>微信文章页面</title>
    </head>
    <body>    """
    fh=open("D:/untitled6/wechat crawl/1.html","wb")
    fh.write(html1.encode("utf-8"))
    fh.close()
    fh=open("D:/untitled6/wechat crawl/1.html","ab")

    urllist=urlcontent(proxy_addr,page)     #文章的网址
    print(len(urllist)-1)
    for i in range(0,len(urllist)-1):
        trueurllist=urllist[i].replace("amp;","")
        urldata=urllib.request.urlopen(trueurllist).read().decode("utf-8") #相对应内容所对应的网址内容列表
        titlepat="<title>(.*?)</title>"
        contentpat='id="js_content">([\s\S]*?)id="js_sg_bar"'
        titlecollection=re.compile(titlepat).findall(urldata,re.S)
        contentcollection=re.compile(contentpat).findall(urldata,re.S)

        print(trueurllist)
        print(titlecollection)
        print(contentcollection)
        dataall="<p>标题为："+titlecollection[0]+"</p><p>内容为"+contentcollection[0]+"</p><br>"
        fh.write(dataall.encode("utf-8"))
    fh.close()
    html2="""
            </body>
        </html>"""
    fh=open("D:/untitled6/wechat crawl/1.html","ab")
    fh.write(html2.encode("utf-8"))
    fh.close()
proxy_addr="121.238.3.218:8118"
page=1
getcontent(proxy_addr,page)
