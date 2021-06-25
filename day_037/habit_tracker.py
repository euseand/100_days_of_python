import requests


USERNAME = "eugeneatpixela"
TOKEN = "eugeneatpixela"
USER_URL = "https://pixe.la/v1/users"
GRAPH_URL = f"{USER_URL}/{USERNAME}/graphs"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

graph_params = {
    "id": "weightgraph1",
    "name": "Sample Weight Graph",
    "unit": "Kg",
    "type": "float",
    "color": "shibafu",
}

pixel_params = {
    "date": "20210623",
    "quantity": "72.0",
}

response = requests.post(GRAPH_URL + "/weightgraph1", json=pixel_params, headers=headers).text
print(response)

