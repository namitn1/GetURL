from bs4 import BeautifulSoup

import requests

url = raw_input("Enter URL")
r = requests.get("http://" + url)
data = r.text
a = BeautifulSoup(data);

for link in a.find_all('a'):
    print(link.get('href'))
