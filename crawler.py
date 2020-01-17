import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError
from urllib.parse import urljoin
from urllib import robotparser
import  re
import itertools

def Download(url, num_retries = 2, user_agent = 'wswp', charset = 'utf-8'):
    print('Downloading: ',url)
    request = urllib.request.Request(url)
    request.add_header('User_agent', user_agent)
    try:
        resp = urllib.request.urlopen(request)
        cs = resp.headers.get_content_charset()
        if not cs:
            cs = charset
        html = resp.read().decode(cs)
        #html = urllib.request.urlopen(url).read()
    except (URLError, HTTPError, ContentTooShortError) as error:
        print('Downloading error: ', error.reason)
        html = None
        if num_retries > 0:
            if hasattr(error, 'code') and 500 <= error.code < 600:
                return download(url, num_retries-1)
   # print(html)
    return html

def GetRobotsParser(robots_url):
    rp = robotparser.RobotFileParser()
    rp.set_url(robots_url)
    rp.read()
    return rp                                

def CrawlSitemap(url):
    #Download the sitemap file
    sitemap = Download(url)
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    print(links)
    for link in links:
        print(link)
        html = Download(link)
        print(html+'\n\n\n\n')

def LinkCrawler(start_url,link_regex):
    crawl_queue = [start_url]
    print(crawl_queue)
    seen = set(crawl_queue)
    while crawl_queue:
        url = crawl_queue.pop()
        print("queue: "+url)
        html = Download(url)
        if not html:
            #print(html)
            continue
        for link in get_links(html):
            if re.match(link_regex,link):
                abs_link = urljoin(start_url,link)
                if abs_link not in seen:
                    seen.add(abs_link)
                    crawl_queue.append(abs_link)

def get_links(html):
    webpage_regex = re.compile("""<a[^>]>+href=["'](.*?)["']""",re.IGNORECASE)
    print("get_links()!!!")
    print(webpage_regex.findall(html))
    return webpage_regex.findall(html)
    

def GetUrl():
    url_head = "https://"
    url_body = input("Input url: ")
    url = url_head + url_body
    return url_body

def SaveHtml(FileName,FileContent):
    with open(FileName,"wb") as f:
        f.write(FileContent)


def main():
    url = GetUrl()
    LinkCrawler(url,'/(index|view)/')
   # html = Download(url)
   # SaveHtml("bing",html)
   #CrawlSitemap(url)
   #print(html)


main()
