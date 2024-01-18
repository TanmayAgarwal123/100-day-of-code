import requests

USERNAME = "tanmay10"
TOKEN = "tanmayagarwal"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": USERNAME,
    "username": TOKEN,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "ajisai",
}
requests.post(url=graph_endpoint, json=graph_config, headers=headers)
