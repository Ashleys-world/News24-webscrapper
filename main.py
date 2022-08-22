import requests

from bs4 import BeautifulSoup

import datetime

now = datetime.datetime.now()

content = ''

def extract_news(url):
    print('Extracting top stories from news24')
    cnt = ''
    cnt2 = ''
    cnt += ('Top stories : \n')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    for i,tag in enumerate(soup.find_all('div',attrs={'class':'article-item__title'})):
        cnt += ((str(i+1)+tag.span.string ) if i < 10 else '')
        #print(tag.prettify)
    return(cnt)

cnt = extract_news('https://www.news24.com/news24/southafrica')
content += cnt

print(content)

