from fastapi import FastAPI
#import datascrape


# app_dic = datascrape.airline_dic
#print(app_dic)
app_dic = {
    'origin': {0: 'KHI', 1: 'KHI', 2: 'KHI', 3: 'KHI'},
    'destination': {0: 'SYD', 1: 'SYD', 2: 'SYD', 3: 'SYD'},
           }                                                                                                                                                                                                
app = FastAPI()

@app.get("/ticketprice")
def ticket_price():
    return app_dic




