import requests
from datetime import datetime

USERNAME = "vof"
GRAPH_ID = "graph1"
TOKEN = "uofhhlguohgghhgghgkgkklgk"
pixela_url = "https://pixe.la/v1/users"
pixela_param = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}

today = datetime.now()

#response = requests.post(pixela_url, json=pixela_param)
# print(response.text)
# print(response)
#
pixela_graph_url = f"{pixela_url}/{USERNAME}/graphs"
# # graph_param = {
# #     "id": GRAPH_ID,
# #     "name": "Coding Graph",
# #     "unit": "Hour",
# #     "type": "float",
# #     "color": "sora"
# # }
# #
headers = {
    "X-USER-TOKEN": TOKEN
}
# #
# # response = requests.post(url=pixela_graph_url, json=graph_param, headers=headers)
# # print(response.text)
#
input_url = f"{pixela_graph_url}/{GRAPH_ID}"
print(today.strftime("%Y%m%d"))
#
graph_input = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you code today? ")
}
response = requests.post(url=input_url, json=graph_input, headers=headers)
print(response.text)

# change_url = f"{input_url}/{yesterday}"
# change_input = {
#     "quantity": "20.5"
# }
# #response = requests.put(url=change_url, json=change_input, headers=headers)
# #print(response.text)
#
# # response = requests.delete(url=change_url, headers=headers)
# # print(response.text)