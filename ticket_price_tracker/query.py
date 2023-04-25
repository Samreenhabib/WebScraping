from flask import Flask, request, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)


@app.route('/<path:route>', methods = ['GET'])
def query_example(route):
    # if key doesn't exist, returns None
    sort = request.args.get('sort')
    route = request.path
    query =  dict()
    query['sort'] = sort
    query['route'] = route
    return render_template('queryresult.html', data=query)


    return 
    

    # htmlSourceCode = getHtmlSourceCode(route)
    # soup = BeautifulSoup(htmlSourceCode, 'html.parser')
    # print(soup.prettify())

if __name__ == '__main__':
    app.run(debug=True, port=5000)


# from urllib.parse import urlparse, parse_qs
# url = "https://www.kayak.com/flights/KHI-SYD/2023-05-05?sort=price_a"

# parsed_url = urlparse(url)
# query_params = parse_qs(parsed_url.query)
# print(query_params)
# # Extract the path component from the parsed URL
# path = parsed_url.path
# # print(path)
# # # Split the path by '/' to extract the origin and destination values
# origin_destination, date = path.split('/')[2:]
# origin = origin_destination.split('-')[0]
# destination = origin_destination.split('-')[1]
# print("Origin:", origin)
# print("Destination:", destination)
# print("Date:", date)