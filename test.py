import requests
import logging
import json

def fetch_and_store_data():
    logging.info('fetch_and_store_data started')
    response = requests.get('https://publicapi.battlebit.cloud/Servers/GetServerList')
    response.raise_for_status()  # Optional, but good practice to ensure a valid response
    data = response.json()
    for item in data:
        print(item.get('Name'))
    logging.info('fetch_and_store_data finished')

fetch_and_store_data()