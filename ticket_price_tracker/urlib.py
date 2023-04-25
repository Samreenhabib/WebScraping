from bs4 import BeautifulSoup
from urllib.request import urlopen
import time 
origin = "KHI"
destination = "SYD"
startdate = '2023-05-01'
url = "https://www.kayak.com/flights/" + origin + "-" + destination + "/" + startdate + "?sort=bestflight_a&"

page = urlopen(url)
html = page.read().decode("utf-8")
time.sleep(20)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
prices = soup.find_all('div', attrs={'class': 'f8F1-price-text'})
price_list = []
    
for div in prices:
    price = div.getText()
    price_list.append(price)

print(price_list)