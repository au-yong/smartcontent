from imagedetect import GetImageInfo
import requests
import json
import random

def get_news_with_category(search_term):
    news_url = "https://newsapi.org/v2/top-headlines?q=%s&apiKey=913bf17a0dde43ada64c47e4bf3a1461" % (search_term)
    response = requests.get(news_url)
    return response.json().get('articles')

def generate_news_posts(imageUrl):
    image_content = GetImageInfo().info(imageUrl)
    news_post = []
    for term in image_content[1]:
        news = get_news_with_category(term)
        news_post += news
    return news_post
print(GetImageInfo().info('data/cat.jpg'))
# with open('quotes.json',"r") as file:
#     quotes = json.load(file)
#     quote_contents = ""
#     for quote in quotes:
#         quote_contents += quote.get('content') + "\n"
#         # + " " + quote.get('author') + " " + str(random.randint(1,50000)) +
# with open("data/quotes_data_train.txt","w")  as writefile:    
#     writefile.write(quote_contents)    



