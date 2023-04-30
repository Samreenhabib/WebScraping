from flask import Flask, request, render_template
from bs4 import BeautifulSoup
import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)


@app.route('/<path:route>', methods = ['GET'])
def query_example(route):
    
    sort = request.args.get('sort')
    route = request.path
    parts = route.split("/")
    origin = parts[1][:3]
    destination = parts[1][4:] 
    date = parts[2]
    query =  dict()
    query['origin'] = origin
    query['destination'] = destination
    query['date'] = date
    query['sort'] = sort

    url = "https://www.kayak.com/flights/" + origin + "-" + destination + "/" + date + sort
    query['url'] = url

    driver = webdriver.Chrome()
    # options = Options()
    # options.add_argument('--headless')
    # driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)

    driver.get(url)
    #Check if Kayak thinks that we're a bot
    time.sleep(3) 
    soup=BeautifulSoup(driver.page_source, 'lxml')

    if soup.find_all('p')[0].getText() == "Please confirm that you are a real KAYAK user.":
        print("Kayak thinks I'm a bot, which I am ... so let's wait a bit and try again")
        driver.close()
        time.sleep(10)

    time.sleep(5)

    soup=BeautifulSoup(driver.page_source, 'lxml')
    prices = soup.find_all('div', attrs={'class': 'f8F1-price-text'})
    time_slot = soup.find_all('div', attrs={'class':'VY2U'})
    price_list = []
    dpt_list = []
    av_time_list = []
    for div in prices:
        price = div.getText()
        price_list.append(price)

    for s in time_slot:
        span_ele = s.find_all('span')
        dept_time = span_ele[0].text
        dpt_list.append(dept_time)
        arrival_time = span_ele[2].text
        av_time_list.append(arrival_time)

    df = pd.DataFrame({"origin" : origin , "destination" : destination ,
                       "startdate" : date,
                        "price" : price_list,
                         "deptime" : dpt_list,
                          "arrtime" : av_time_list })

    airline_dic = df.to_dict()
    
    dic_1 = {"origin" : origin , "destination" : destination ,
                       "startdate" : date,
                        "price" : price_list,
                         "deptime" : dpt_list,
                          "arrtime" : av_time_list }
    return dic_1

#     return render_template('queryresult.html', query=query, flight_details=airline_dic)
    

if __name__ == '__main__':
    app.run(debug=True, port=5000)
