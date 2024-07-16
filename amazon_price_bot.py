import requests as r
import bs4
from datetime import datetime
import time
import schedule

product_list = ['B09SPN8F23'] # Enter the ID of the products you wish to keep a track of
base_url = 'https://www.amazon.in'
url = 'https://www.amazon.in/dp/'

header= {
    # 'user-agent': 'Enter your user agent here'
}
base_response = r.get(base_url, headers = header)
cookies = base_response.cookies

def track_prices():
    print(datetime.now())
    for prod in product_list:
        product_Response = r.get(url + prod ,
                                headers= header,
                                cookies= cookies)

        soup = bs4.BeautifulSoup(product_Response.text, features= "html.parser")
        price_lines = soup.findAll(class_ = "a-price-whole" )

        final_price = str(price_lines[0])
        final_price = final_price.replace('<span class="a-price-whole">', '')
        final_price = final_price.replace('<span class="a-price-decimal">.</span></span>', '')

        print(url + prod, final_price)

schedule.every(1).hour.do(track_prices)

while True:
    schedule.run_pending()
    time.sleep(1)