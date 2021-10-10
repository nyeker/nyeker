# Python program to extract all links from a web page using BeautifulSoup 4.


from bs4 import BeautifulSoup, SoupStrainer
import requests
url = input('Enter - ')
#url = "http://python.org/"
page = requests.get(url)
data = page.text
soup = BeautifulSoup(data)
for link in soup.find_all('a'):
    print(link.get('href'))
