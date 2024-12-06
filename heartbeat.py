import requests
import time

servers = ["http://localhost:5001", "http://localhost:5002"]

def check_servers():
    for server in servers:
        try:
            response = requests.get(server)
            if response.status_code == 200:
                print(f"{server} is UP")
            else:
                print(f"{server} returned error code: {response.status_code}")
        except requests.exceptions.RequestException:
            print(f"{server} is DOWN")

while True:
    check_servers()
    time.sleep(10)