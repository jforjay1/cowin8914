import requests
import json
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
url = "https://cdn-api.co-vin.in/api/v2/admin/location/districts/11"
response = requests.get(url,headers=header)
print(response.json())