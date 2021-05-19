import requests

base_url  = "https://localhost"
endpoint = "/endpoint"

api_key = "KEY"

payload = {
    'key': api_key,
    'q':"X"
}

response = requests.get(base_url+endpoint, params=payload)

if response.status_code == requests.codes.ok:
    data = response.json()
    print(data)
else:
    print(response.status_code)
    print(response.text)