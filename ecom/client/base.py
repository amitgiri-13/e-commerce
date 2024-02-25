import requests

endpoint = "http://127.0.0.1:8000/api/products/33/"
endpoint2 = "http://127.0.0.1:8000/api/users/7/"

product_data =   {
        "category": 8,
        "owner": 10,
        "product": "funky cap ",
        "description": "-look stylish",
        "price": "399",
        "created_at": "2024-02-18T09:49:42.891746+05:45",
        "in_stock": False
    }


files = {
    "image" : open("./images/funnycap.jpeg","rb")
}
user_data =   {
        "id": 13,
        "username": "supreme",
        "products": []
    }
response = requests.delete(endpoint,data=product_data,files=files,auth=("mahakmaha","!@#123ASDasd"))
#response = requests.post(endpoint2,data = user_data,auth=("amit","!@#123ASDasd"))
print(response)