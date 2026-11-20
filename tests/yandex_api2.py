import requests

BASE_URL = "https://yandex.net"

def create_folder(token, folder_name):
    headers = {"Authorization": f"OAuth {token}"}
    params = {"path": folder_name}
    response = requests.put(BASE_URL, headers=headers, params=params)
    return response.status_code

def check_folder_exists(token, folder_name):
    headers = {"Authorization": f"OAuth {token}"}
    params = {"path": folder_name}
    response = requests.get(BASE_URL, headers=headers, params=params)
    return response.status_code

def delete_folder(token, folder_name):
    headers = {"Authorization": f"OAuth {token}"}
    params = {"path": folder_name, 'permanently': 'true'}
    response = requests.delete(BASE_URL, headers=headers, params=params)
    return response.status_code
