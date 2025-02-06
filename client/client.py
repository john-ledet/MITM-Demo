import requests
import time

#MITM proxy
proxy = {
    "http":"http://mitm:8080",
    "https": "http://mitm:8080"
}

#server 
server = "http://server:5000/login"

#login credentials
credentials = {
    "username" : "admin",
    "password" : "password"
}

while True:
    try:
        response = requests.post(server, data=credentials, proxies=proxy, verify=False)
        print(f"Server Response: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

    time.sleep(10)  # Send request every 10 seconds