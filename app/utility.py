import os
import requests
from dotenv import load_dotenv
load_dotenv()

def initialize_test_connection():
    response = requests.post(f"{os.environ.get('API_CONNECTION')}/initialize")
    if response.status_code == 200:
        connection_id = response.json().get("connection_id")
    else:
        raise Exception("Failed to initialize connection with the API")
    return connection_id