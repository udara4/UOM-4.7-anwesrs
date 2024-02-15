# # print('test')
# tet_snak = 'priyatha maha'
# print(tet_snak)
# test_number = 25
# print(test_number)
# def say_bane(name):
#     print(name)

# say_bane('udara')

# def print_name(name='test'):
#     print(name)

# print_name('udara')
# def print_hi_with_name(greet,name=' test'):
#     if greet=='SIR':{
#         print(f'hey ? {name}')

#     }
#     elif greet == 'Miss':{
#             print(f'hey miss ? {name}')
#         }
#     else:{print(f'buy ? {name}')}

    
# print_hi_with_name('SIR','udara')
# print_hi_with_name('Miss','Nuwani')
# print_hi_with_name('','udara')

# def weather(condition):
#     if condition=="Rain":
#         print('rain')
#     else:
#         print('clear')

# weather('Rain')



# def sum(a,b):
#     return a + b

# print(sum(2,3))

# def food_commision(presentage,food):
#     print(f'food price $ {food}')
#     print(f'Commision % {presentage}')
    
#     commision = food*(presentage/100)
#     total= food + commision
#     print(f'total price {total}')
    
# food_commision(10,50)


# def calculate_age(age):
#     if age <= 18:
#         return 'You are teen'
#     elif age == 18:
#         return 'You are young'
#     else:
#         return 'You are old'
    
# print(calculate_age())
# def positive(num):
#     if num>0:
#         print('positive number')
#     elif num==0:
#         print('number is Zero')
#     else:
#         print('negative number')
# positive(-1)
# def devisible(num):
#     if num % 2 == 0:
#         if num % 3 == 0:
#             return 'devisible in three and two'
#         else:
#             return 'only divisible in two'
#     else:
#         return 'Canot divisible in three and two'
# print(devisible(5))
# def tinery(age):
#     status = 'adulut' if age >=18 else 'teen'
#     print(f'you consider as {status}')



# tinery(12)
# len ([1,2,3,4])
# import requests
# import json

# # Update the product data with the new brand name
# product_data = {
#     "productName": "Araliya Basmathi Rice",
#     "description": "White Basmathi Rice imported from Pakistan. High-quality rice with extra fragrance. Organically grown.",
#     "category": "Rice",
#     "brand": "Araliya",  # Updated brand name
#     "expiredDate": "2023.05.04",
#     "manufacturedDate": "2022.02.20",
#     "batchNumber": 324567,
#     "unitPrice": 1020,
#     "quantity": 200,
#     "createdDate": "2022.02.24"
# }

# # Base URL for the API
# base_url = "http://host1.open.uom.lk:8080"

# # URL for updating a product
# update_product_url = f"{base_url}/api/products/"

# # Send a PUT request to update the product
# response = requests.put(update_product_url, json=product_data)

# # Check for successful response
# if response.status_code == 200:
#     # Print the JSON response
#     print(json.dumps(response.json(), indent=4))
# else:
#     print(f"Error updating product: {response.status_code}")

#  ==============answer1=============        
import requests
base_url = 'http://host1.open.uom.lk:8080'
product = {
"productName":"Araliya Basmathi Rice",
"description":"White Basmathi Rice imported from Pakistan. High-quality rice with extra fragrance. Organically grown.",
"category":"Rice",
"brand":"CIC",
"expiredDate":"2023.05.04",
"manufacturedDate":"2022.02.20",
"batchNumber":"324567",
"unitPrice":"1020",
"quantity":"200",
"createdDate":"2022.02.24"
}

response = requests.post(f"{base_url}/api/products/")
data =response.json()
print(response.status_code)
# ============anser2==============

import requests

base_url = 'http://host1.open.uom.lk:8080'

response = requests.get(f"{base_url}/api/products/")
data = response.json()

#data =>
#{'message': 'success', 'data': [{'id': 680, 'productName': 'Araliya Basmathi Rice', 'description': 'White Basmathi Rice imported from Pakistan. High-quality rice with extra fragrance. Organically grown.', 'category': 'Rice', 'brand': 'Araliya', 'expiredDate': '2023.05.04', 'manufacturedDate': '2022.02.20', 'batchNumber': 324567, 'unitPrice': 1020, 'quantity': 200, 'createdDate': '2022.02.24'}, {'id': 686, 'productName': 'Araliya Basmathi Rice', 'description': 'White Basmathi Rice imported from Pakistan. High-quality rice with extra fragrance. Organically grown.', 'category': 'Rice', 'brand': 'CIC', 'expiredDate': '2023.05.04', 'manufacturedDate': '2022.02.20', 'batchNumber': 324567, 'unitPrice': 1020, 'quantity': 200, 'createdDate': '2022.02.24'}]}


products = data['data']
print(len(products))
# ===========anser3===========
BASE_URL = 'http://host1.open.uom.lk:8080'

new_product = {
"productName":"Araliya Basmathi Rice",
"description":"White Basmathi Rice imported from Pakistan. High-quality rice with extra fragrance. Organically grown.",
"category":"Rice",
"brand":"Araliya",
"expiredDate":"2023.05.04",
"manufacturedDate":"2022.02.20",
"batchNumber":324567,
"unitPrice":1020,
"quantity":200,
"createdDate":"2022.02.24"
}

response = requests.put('http://host1.open.uom.lk/api/products/', json=new_product)
print(response.json())