import requests

endpoint1 = "http://127.0.0.1:8000/api/orders/"
endpoint2 = "http://127.0.0.1:8000/api/orders/44/"

pranisha = ("pranisha","!@#123ASDasd")
supreme = ("supreme","!@#123ASDasd")
mahak = ("mahakmaha","!@#123ASDasd")
amit = ("amit","!@#123ASDasd")

data = {
    "id": 44,
    "product": 29,
    "quantity": 1,
    "order_status": "CN",
    "payment_status": True,
    "order_date": "2024-02-26T08:18:38.731590+05:45",
    "order_address": "Nepal",
    "receiver_name": "Amit Giri",
    "contact_number": 9847630534,
    "total_price": 400.0
}

def get(endpoint,auth):
    response = requests.get(endpoint,auth=auth)
    data = (response.json())
    print(data)
    for index,i in enumerate(data):
        print(index+1,i)
        print()

response = requests.put(endpoint2,data,auth=mahak)
print(mahak)
print(response.json())