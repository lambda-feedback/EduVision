import requests

def initialize_test_connection():
    response = requests.post(f"http://20.117.225.136:8000/initialize")
    if response.status_code == 200:
        connection_id = response.json().get("connection_id")
    else:
        raise Exception("Failed to initialize connection with the API")
    return connection_id