import requests
from bs4 import BeautifulSoup

url = "https://www.google.com"
response = requests.get(url)

# print(response.text)
print(type(response.text))

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())

for heading in soup.find_all("h"):
    print(heading.text)