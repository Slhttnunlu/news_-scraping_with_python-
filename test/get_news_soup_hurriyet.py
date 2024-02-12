import requests
from bs4 import BeautifulSoup

def get_news(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        print("---http request 200---")
        
        title = soup.find('h1', class_='news-detail-title')
        #print(title)
        news_intro = soup.find('div', class_='news-content__inf').find('h2')
        #print(news_intro)
        content_paragraphs = soup.find('div', class_='news-content readingTime').find_all('p')
        #print(content_paragraphs)

        title = title.text
        news_intro = news_intro.text
        content = ''
        for paragraph in content_paragraphs:
            #print(type(paragraph))
            content += paragraph.text + '\n'
        #content = strip_html_tags(content)
        #print(type(content))

        print("title : " + title)
        print("content : " + news_intro)
        print(content)

url = 'https://www.hurriyet.com.tr/gundem/kucukcekmecedeki-silahli-saldiri-cumhurbaskani-erdogan-bir-tanesi-yakalandi-digerlerini-de-yakalayacagiz-42404416'

get_news(url)