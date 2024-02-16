# # # print('test')
# # tet_snak = 'priyatha maha'
# # print(tet_snak)
# # test_number = 25
# # print(test_number)
# # def say_bane(name):
# #     print(name)

# # say_bane('udara')

# # def print_name(name='test'):
# #     print(name)

# # print_name('udara')
# # def print_hi_with_name(greet,name=' test'):
# #     if greet=='SIR':{
# #         print(f'hey ? {name}')

# #     }
# #     elif greet == 'Miss':{
# #             print(f'hey miss ? {name}')
# #         }
# #     else:{print(f'buy ? {name}')}

    
# # print_hi_with_name('SIR','udara')
# # print_hi_with_name('Miss','Nuwani')
# # print_hi_with_name('','udara')

# # def weather(condition):
# #     if condition=="Rain":
# #         print('rain')
# #     else:
# #         print('clear')

# # weather('Rain')



# # def sum(a,b):
# #     return a + b

# # print(sum(2,3))

# # def food_commision(presentage,food):
# #     print(f'food price $ {food}')
# #     print(f'Commision % {presentage}')
    
# #     commision = food*(presentage/100)
# #     total= food + commision
# #     print(f'total price {total}')
    
# # food_commision(10,50)


# # def calculate_age(age):
# #     if age <= 18:
# #         return 'You are teen'
# #     elif age == 18:
# #         return 'You are young'
# #     else:
# #         return 'You are old'
    
# # print(calculate_age())
# # def positive(num):
# #     if num>0:
# #         print('positive number')
# #     elif num==0:
# #         print('number is Zero')
# #     else:
# #         print('negative number')
# # positive(-1)
# # def devisible(num):
# #     if num % 2 == 0:
# #         if num % 3 == 0:
# #             return 'devisible in three and two'
# #         else:
# #             return 'only divisible in two'
# #     else:
# #         return 'Canot divisible in three and two'
# # print(devisible(5))
# # def tinery(age):
# #     status = 'adulut' if age >=18 else 'teen'
# #     print(f'you consider as {status}')



# # tinery(12)
# # len ([1,2,3,4])
# # import requests
# # import json

# # # Update the product data with the new brand name
# # product_data = {
# #     "productName": "Araliya Basmathi Rice",
# #     "description": "White Basmathi Rice imported from Pakistan. High-quality rice with extra fragrance. Organically grown.",
# #     "category": "Rice",
# #     "brand": "Araliya",  # Updated brand name
# #     "expiredDate": "2023.05.04",
# #     "manufacturedDate": "2022.02.20",
# #     "batchNumber": 324567,
# #     "unitPrice": 1020,
# #     "quantity": 200,
# #     "createdDate": "2022.02.24"
# # }

# # # Base URL for the API
# # base_url = "http://host1.open.uom.lk:8080"

# # # URL for updating a product
# # update_product_url = f"{base_url}/api/products/"

# # # Send a PUT request to update the product
# # response = requests.put(update_product_url, json=product_data)

# # # Check for successful response
# # if response.status_code == 200:
# #     # Print the JSON response
# #     print(json.dumps(response.json(), indent=4))
# # else:
# #     print(f"Error updating product: {response.status_code}")

# #  ==============answer1=============        
# import requests
# base_url = 'http://host1.open.uom.lk:8080'
# product = {
# "productName":"Araliya Basmathi Rice",
# "description":"White Basmathi Rice imported from Pakistan. High-quality rice with extra fragrance. Organically grown.",
# "category":"Rice",
# "brand":"CIC",
# "expiredDate":"2023.05.04",
# "manufacturedDate":"2022.02.20",
# "batchNumber":"324567",
# "unitPrice":"1020",
# "quantity":"200",
# "createdDate":"2022.02.24"
# }

# response = requests.post(f"{base_url}/api/products/")
# data =response.json()
# print(response.status_code)
# # ============anser2==============

# import requests

# base_url = 'http://host1.open.uom.lk:8080'

# response = requests.get(f"{base_url}/api/products/")
# data = response.json()

# #data =>
# #{'message': 'success', 'data': [{'id': 680, 'productName': 'Araliya Basmathi Rice', 'description': 'White Basmathi Rice imported from Pakistan. High-quality rice with extra fragrance. Organically grown.', 'category': 'Rice', 'brand': 'Araliya', 'expiredDate': '2023.05.04', 'manufacturedDate': '2022.02.20', 'batchNumber': 324567, 'unitPrice': 1020, 'quantity': 200, 'createdDate': '2022.02.24'}, {'id': 686, 'productName': 'Araliya Basmathi Rice', 'description': 'White Basmathi Rice imported from Pakistan. High-quality rice with extra fragrance. Organically grown.', 'category': 'Rice', 'brand': 'CIC', 'expiredDate': '2023.05.04', 'manufacturedDate': '2022.02.20', 'batchNumber': 324567, 'unitPrice': 1020, 'quantity': 200, 'createdDate': '2022.02.24'}]}


# products = data['data']
# print(len(products))
# # ===========anser3===========
# BASE_URL = 'http://host1.open.uom.lk:8080'

# new_product = {
# "productName":"Araliya Basmathi Rice",
# "description":"White Basmathi Rice imported from Pakistan. High-quality rice with extra fragrance. Organically grown.",
# "category":"Rice",
# "brand":"Araliya",
# "expiredDate":"2023.05.04",
# "manufacturedDate":"2022.02.20",
# "batchNumber":324567,
# "unitPrice":1020,
# "quantity":200,
# "createdDate":"2022.02.24"
# }

# response = requests.put('http://host1.open.uom.lk/api/products/', json=new_product)
# print(response.json())
import requests
import json
from bs4 import BeautifulSoup

# Imitate the Mozilla browser.
user_agent = {'User-agent': 'Mozilla/5.0'}

def compare_prices(laughs_product, glomark_product):
    # Acquire the web pages which contain product Price
    laughs_response = requests.get(laughs_product)
    glomark_response = requests.get(glomark_product)

    # LaughsSuper supermarket website provides the price in a span text.
    soup_laughs = BeautifulSoup(laughs_response.text, 'html.parser')
    price_span = soup_laughs.find('span', {'class': 'price'})
    if price_span:
        price_laughs = price_span.text.strip()
    else:
        price_laughs = "Price not found"

    product_name_laughs = soup_laughs.find('span', {'class': 'sku-no'}).text.strip()

    # Glomark supermarket website provides the data in JSON format in an inline script.
    soup_glomark = BeautifulSoup(glomark_response.text, 'html.parser')
    script_glomark = soup_glomark.find('script', {'type': 'application/ld+json'}).text
    data_glomark = json.loads(script_glomark)
    price_glomark = data_glomark['offers'][0]['price']

    # Parse the values as floats
    if price_laughs != "Price not found":
        price_laughs = float(price_laughs.replace("Rs.", "").strip())
    else:
        price_laughs = 0.0
    price_glomark = float(price_glomark)

    # Compare the prices and create the comparison result string
    comparison_result = f'{product_name_laughs} Rs.: {price_laughs}\n'
    comparison_result += f'Glomark Rs.: {price_glomark}\n'

    if price_laughs > price_glomark:
        comparison_result += f'Laughs is cheaper Rs.: {price_laughs - price_glomark}'
    elif price_laughs < price_glomark:
        comparison_result += f'Glomark is cheaper Rs.: {price_glomark - price_laughs}'
    else:
        comparison_result += 'Price is the same'

    return comparison_result

laughs_coconut = 'https://scrape-sm1.github.io/site1/COCONUT%20market1super.html'
glomark_coconut = 'https://glomark.lk/coconut/p/11624'
print("Coconut Comparison:")
print(compare_prices(laughs_coconut, glomark_coconut))

laughs_tissues = 'https://scrape-sm1.github.io/site1/FLORA%20FACIAL%20TISSUES%202%20X%20160%20BOX%20-%20HOUSEHOLD%20-%20Categories%20market1super.com.html'
glomark_tissues = 'https://glomark.lk/flora-facial-tissues-160s/p/10470'
print("\nTissues Comparison:")
print(compare_prices(laughs_tissues, glomark_tissues))

laughs_bread = 'https://scrape-sm1.github.io/site1/Crimson%20Bread%20Sliced%20market1super.com.html'
glomark_bread = 'https://glomark.lk/sandwich-bread-450g/p/13606'
print("\nBread Comparison:")
print(compare_prices(laughs_bread, glomark_bread))
