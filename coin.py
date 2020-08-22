from bs4 import BeautifulSoup
import urllib.parse
import urllib.request
import requests
search = 'Dollar'
searchPenCode = urllib.parse.quote_plus(search)
url = 'https://www.google.com/search?q='+searchPenCode
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
title = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'})
print(title.text)
# print(soup.prettify())
