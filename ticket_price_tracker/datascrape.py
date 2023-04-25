import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

origin = "KHI"
destination = "SYD"
# startdate = datetime.now()
# startdate = startdate.strftime("%Y-%m-%d")
startdate = '2023-05-01'
url = "https://www.kayak.com/flights/" + origin + "-" + destination + "/" + startdate + "?sort=bestflight_a&"
# print(url)
driver = webdriver.Chrome()
# options = Options()
# options.add_argument('--headless')
# driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)

driver.get(url)
#Check if Kayak thinks that we're a bot
time.sleep(5) 
soup=BeautifulSoup(driver.page_source, 'lxml')

if soup.find_all('p')[0].getText() == "Please confirm that you are a real KAYAK user.":
    print("Kayak thinks I'm a bot, which I am ... so let's wait a bit and try again")
    driver.close()
    time.sleep(20)

time.sleep(5)

soup=BeautifulSoup(driver.page_source, 'lxml')

# print(soup.prettify())
#get the arrival and departure times
prices = soup.find_all('div', attrs={'class': 'f8F1-price-text'})
#print(prices)

time_slot = soup.find_all('div', attrs={'class':'VY2U'})
print(time_slot)
# price_list = []
# dpt_list = []
# av_time_list = []
# for div in prices:
#     price = div.getText()
#     price_list.append(price)

# for s in time_slot:
#     span_ele = s.find_all('span')
#     dept_time = span_ele[0].text
#     dpt_list.append(dept_time)
#     arrival_time = span_ele[2].text
#     av_time_list.append(arrival_time)

# df = pd.DataFrame({"origin" : origin , "destination" : destination ,
#                    "startdate" : startdate,
#                     "price" : price_list,
#                      "deptime" : dpt_list,
#                       "arrtime" : av_time_list })

# #print(df)

# airline_dic = df.to_dict()
# print('dic:' , airline_dic)