import requests
from bs4 import BeautifulSoup

def take_link(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        print("---http request 200---")
        
        link_lists = []

        linkler = soup.find('div', class_='swiper-wrapper').find_all('a', class_='img-holder square')
        #linkler = soup.find_all('a', class_='img-holder square')
        print("hurriyet link count:", len(linkler))
        for link in linkler:
            href = link.get('href')
            link_lists.append(href)

        return link_lists

    else:
        print("HTTP request fail. code:", response.status_code)
        return None

# Belirli bir site için linkleri al
url = "https://www.sozcu.com.tr"
links = take_link(url)
if links:
    for link in links:
        if 'http' not in link: 
            link = url + link 
            print(link)
