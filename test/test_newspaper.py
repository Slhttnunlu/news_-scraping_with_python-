from newspaper import Article

url = 'https://www.sozcu.com.tr/kayip-hamile-kadin-ile-2-cocugu-oldurulmus-halde-bulundu-p21781'

article = Article(url)
article.download()

article.parse()

title = article.title
content = article.text

print("Başlık:", title)
print("İçerik:", content)
