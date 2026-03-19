import requests
import os
from dotenv import load_dotenv


load_dotenv()

yd_token = os.getenv("YD_TOKEN")

def create_folder_yd(path):
    url_yd = "https://cloud-api.yandex.net/v1/disk/resources"
    params = {'path': path}
    headers = {'Authorization': f'OAuth {yd_token}'}
    response = requests.put(url_yd, params=params, headers=headers)

    return response.status_code

create_folder_yd('yd_folder')
