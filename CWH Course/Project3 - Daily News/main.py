# DAILY NEWS

import requests

query = input("Enter the topic of news you want to view: ")
num = int(input(f"How many news articles do you want on the topic of '{query}'? "))

url = f"https://newsapi.org/v2/everything?q={query}&from=2024-07-09&sortBy=publishedAt&apiKey=c024f05bef874b6bbc4837adeb798b78"

response = requests.get(url)
news = response.json()
# print(news)

i = 0
for article in news["articles"]:
    i += 1
    print(f"Article no. {i}\n")
    print(f"Title: {article["title"]}")
    print(f"Published Date: {article["publishedAt"]}")
    print(f"\nDescription:\n{article["description"]}")
    print("-" * 50)
      
    if (i==num):
        break