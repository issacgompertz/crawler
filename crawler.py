import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError

def Download(url, num_retries = 2, user_agent = 'wswp'):
    print('Downloading: ',url)
    request = urllib.request.Request(url)
    request.add_header('User_agent', user_agent)
    try:
        html = urllib.request.urlopen(url).read()
    except (URLError, HTTPError, ContentTooShortError) as error:
        print('Downloading error: ', error.reason)
        html = None
        if num_retries > 0:
            if hasattr(error, 'code') and 500 <= error.code < 600:
                return download(url, num_retries-1)
    return html

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
    html = Download(url)
    SaveHtml("bing",html)
    print(html)

main()
