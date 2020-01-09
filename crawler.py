import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError
import  re

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

def CrawlSitemap(url):
    #Download the sitemap file
    sitemap = Download(url)
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    print(links)
    for link in links:
        print(link)
        html = Download(link)
        print(html+'\n\n\n\n')

def GetUrl():
    url_head = "https://"
    url_body = input("Input url: ")
    url = url_head + url_body
    return url

def SaveHtml(FileName,FileContent):
    with open(FileName,"wb") as f:
        f.write(FileContent)


def main():
    url = GetUrl()
   # html = Download(url)
   # SaveHtml("bing",html)
    CrawlSitemap(url)
#    print(html)

main()
