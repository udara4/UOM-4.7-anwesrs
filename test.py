import requests
import json
import sys
sys.path.insert(0,'bs4.zip')
from bs4 import BeautifulSoup

# Imitate the Mozilla browser.
user_agent = {'User-agent': 'Mozilla/5.0'}

def compare_prices(product_laughs, product_glomark):
    # Acquire the web pages which contain product Price
    laughs_response = requests.get(product_laughs)
    glomark_response = requests.get(product_glomark)

    # LaughsSuper supermarket website provides the price in a span text.
    soup_laughs = BeautifulSoup(laughs_response.text, 'html.parser')
    price_laughs = soup_laughs.findAll('span', {'class': 'price'})[1].text
    product_name_laughs = soup_laughs.find('div', {'class': 'product-name'}).find('h1').text
    
    # Glomark supermarket website provides the product name in a different tag.
    soup_glomark = BeautifulSoup(glomark_response.text, 'html.parser')
    product_name_glomark = soup_glomark.find('div', {'class': 'product-title'}).find('h1').text
    
    # Glomark supermarket website provides the data in JSON format in an inline script.
    script_glomark = soup_glomark.find('script', {'type': 'application/ld+json'}).text
    data_glomark = json.loads(script_glomark)
    
    # Extracting price
    price_glomark = data_glomark['offers'][0].get('price', 'N/A')

    # Parse the values as floats
    price_laughs = float(price_laughs.replace("Rs.", "").strip())
    
    # Convert Glomark price to float if it's not 'N/A'
    if price_glomark != 'N/A':
        price_glomark = float(price_glomark)

    # Print the comparison results
    print('Laughs  ', product_name_laughs, 'Rs.: ', price_laughs)
    print('Glomark ', product_name_glomark, 'Rs.: ', price_glomark)
    
    if price_laughs > price_glomark:
        print('Glomark is cheaper Rs.:', price_laughs - price_glomark)
    elif price_laughs < price_glomark:
        print('Laughs is cheaper Rs.:', price_glomark - price_laughs)
    else:
        print('Price is the same')

# laughs_coconut = 'https://scrape-sm1.github.io/site1/COCONUT%20market1super.html'
# glomark_coconut = 'https://glomark.lk/coconut/p/11624'
# print("Coconut Comparison:")
# compare_prices(laughs_coconut, glomark_coconut)

# laughs_tissues = 'https://scrape-sm1.github.io/site1/FLORA%20FACIAL%20TISSUES%202%20X%20160%20BOX%20-%20HOUSEHOLD%20-%20Categories%20market1super.com.html'
# glomark_tissues = 'https://glomark.lk/flora-facial-tissues-160s/p/10470'
# print("\nTissues Comparison:")
# compare_prices(laughs_tissues, glomark_tissues)

# laughs_bread = 'https://scrape-sm1.github.io/site1/Crimson%20Bread%20Sliced%20market1super.com.html'
# glomark_bread = 'https://glomark.lk/sandwich-bread-450g/p/13606'
# print("\nBread Comparison:")
# compare_prices(laughs_bread, glomark_bread)
