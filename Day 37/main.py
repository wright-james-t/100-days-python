import requests
from dotenv import load_dotenv
import os
from datetime import date

load_dotenv()

PIXELA_TOKEN = os.environ['PIXELA_TOKEN']
PIXELA_USER = 'fuzzy'
GRAPH_ID = 'graph1'

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USER,
    "agreeTermsOfService": 'yes',
    "notMinor": 'yes'

}

graph_config = {
    "id": "graph2",
    "name": "Coding Graph",
    "unit": "Days",
    "type": "int",
    "color": "kuro"
}

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

graph_endpoint = f"{pixela_endpoint}/{PIXELA_USER}/graphs/{GRAPH_ID}"

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers, params=graph_config)
# print(response.text)

formatted_today = str(date.today().strftime("%Y%m%d"))

pixel_post_params = {
    "date": formatted_today,
    "quantity": '1'
}

# post_a_pixel = requests.post(url=graph_endpoint, json=pixel_post_params, headers=headers)

update_params = {
    "quantity": '0'
}

delete_pixel = requests.delete(url=f"{graph_endpoint}/20230422", headers=headers)
print(delete_pixel.text)
