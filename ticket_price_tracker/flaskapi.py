from flask import Flask, render_template
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
app = Flask(__name__)

@app.route('/')
def get_dictionary():
    origin = "KHI"
    destination = "SYD"
    startdate = '2023-05-01'
    url = "https://www.kayak.com/flights/" + origin + "-" + destination + "/" + startdate + "?sort=bestflight_a&"
    
    # options = Options()
    # options.add_argument('--headless')
    # driver = webdriver.Chrome(options=options)

    driver = webdriver.Chrome()
    driver.implicitly_wait(15)
    driver.get(url)

    time.sleep(5)

    soup=BeautifulSoup(driver.page_source, 'lxml')

    if soup.find_all('p')[0].getText() == "Please confirm that you are a real KAYAK user.":
        print("Kayak thinks I'm a bot, which I am ... so let's wait a bit and try again")
        driver.close()
        time.sleep(20)

    time.sleep(5)

    soup=BeautifulSoup(driver.page_source, 'lxml')

    prices = soup.find_all('div', attrs={'class': 'f8F1-price-text'})
    # time_slot = soup.find_all('div', attrs={'class':'VY2U'})

    price_list = []
    # dpt_list = []
    # av_time_list = []
    
    for div in prices:
        price = div.getText()
        price_list.append(price)

    # for s in time_slot:
    #     span_ele = s.find_all('span')
    #     dept_time = span_ele[0].text
    #     dpt_list.append(dept_time)
    #     arrival_time = span_ele[2].text
    #     av_time_list.append(arrival_time)

    # df = pd.DataFrame({"origin" : origin , "destination" : destination ,
    #                 "startdate" : startdate,
    #                     "price" : price_list,
    #                     "deptime" : dpt_list,
    #                     "arrtime" : av_time_list })
    
    df = pd.DataFrame({"origin" : origin , "destination" : destination ,
                    "startdate" : startdate,
                        "price" : price_list })
    
    airline_dic = df.to_dict()
 
    return render_template('results.html', data = airline_dic)

if __name__ == '__main__':
    app.run()