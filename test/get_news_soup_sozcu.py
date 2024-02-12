import requests
from bs4 import BeautifulSoup

def get_news(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        
        title = soup.find('div', class_='news-body').find('h1')
        content_paragraphs = soup.find('div', class_='news-body').find_all('p')
        
        title = title.text
        content = ''
        for paragraph in content_paragraphs:        
            content += paragraph.text + '\n'
        
        print("title : " + title)
        print("content : " + content)
        
url = 'https://www.sozcu.com.tr/kova-da-gezegen-toplasmasi-neler-soyluyor-p21823'


get_news(url)