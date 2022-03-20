# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import requests
from datetime import datetime
USERNAME = "aindrila"
TOKEN = "hgjhjy67245vnfjjjsjfbjvbnfwwrr34"
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": "hgjhjy67245vnfjjjsjfbjvbnfwwrr34",
    "username": "aindrila",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Coding tracker",
    "unit": "commit",
    "type": "int",
    "color": "sora"

}
headers = {
   "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
today = datetime.now()
pixel_creation_endpoint = f"{graph_endpoint}/{graph_config['id']}"
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "5"

}

print(pixel_data['date'])

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
