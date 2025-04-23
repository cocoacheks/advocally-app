import requests

url = "https://www150.statcan.gc.ca/t1/wds/rest/getAllCubesList"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error:", response.status_code)
