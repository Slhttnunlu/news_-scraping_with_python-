import requests
from bs4 import BeautifulSoup
from newspaper import Article
import json
import time

start_time = time.time()

def take_link(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        print("---http request 200---")
        
        link_lists = []

        if 'sozcu.com' in url:
            linkler = soup.find('div', class_='swiper-wrapper').find_all('a', class_='img-holder square')
            print("sozcu link count:", len(linkler))
            for link in linkler:
                href = link.get('href')
                link_lists.append(href)
        elif 'hurriyet.com.tr' in url:
            linkler = soup.find_all('a', class_='home-carousel__slide')
            print("hurriyet link count:", len(linkler))
            for link in linkler:
                href = link.get('href')
                link_lists.append(href)

        return link_lists

    else:
        print("HTTP request fail. code:", response.status_code)
        return None

def get_news_nwsppr(url, website):

    response = requests.get(url)
    
    if response.status_code != 200:
        print("HTTP request failed with code:", response.status_code)
        return None

    article = Article(url)
    article.download()
    article.parse()

    title = article.title
    content = clean_content(article.text)

    data = {
        "website" : website,
        "title": title,
        "content": content
    }

    return data

def get_news_soup(url, website):
    response = requests.get(url)
    
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
    
        try:
            if 'sozcu.com' in website:
                title = soup.find('div', class_='news-body').find('h1')
                content_paragraphs = soup.find('div', class_='news-body').find_all('p')
                content = ''
                
            elif 'hurriyet.com' in website:
                title = soup.find('h1', class_='news-detail-title')
                news_intro = soup.find('div', class_='news-content__inf').find('h2')
                content_paragraphs = soup.find('div', class_='news-content readingTime').find_all('p')
                news_intro = news_intro.text
                content = news_intro + '\n'
                
            title = title.text
            for paragraph in content_paragraphs:        
                content += paragraph.text + '\n'

            data = {
                "website" : website,
                "title " : title,
                "content" : content
            }
            
            return data

        except AttributeError as e:
            #print(url + "----> icerik soup ile alinamadi")
            #print("AttributeError:", e)
            news1 = get_news_nwsppr(url, website)
            if news1:
                news.append(news1)

def clean_content(content):
    return content.replace("Haberin Devamı", "").strip()

urls = ["https://www.sozcu.com.tr", "https://www.hurriyet.com.tr"]
news = []

for url in urls:
    links = take_link(url)
    if links:
        for link in links:
            if 'http' not in link:    
                news1 = get_news_soup(url + link, url)
                if news1 is not None:
                    news.append(news1)

if news:
    print(json.dumps(news, indent=4, ensure_ascii=False))

save_file = input("Do you want to save json datas? (E/H): ").lower()
if save_file == "e":
    file_name = input("Dosya adı: ")
    with open(file_name, "w") as json_file:
        json.dump(news, json_file, indent=4, ensure_ascii=False)
    print("File saved.")
else:
    print("File cant save.")

end_time = time.time()
elapsed_time = end_time - start_time
print("Kodun çalışma süresi:", elapsed_time, "saniye")




