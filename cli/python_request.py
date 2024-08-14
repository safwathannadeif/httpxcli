import requests

url = "http://127.0.0.1:8000/tree_api/qury_prefetch_grp"
headers = {
    "cache-control": "no-cache",
    ##  "x-dreamfactory-api-key": "YOUR_API_KEY"
}
response = requests.request("GET", url, headers=headers)
print(response.status_code)
print(response.content)
#print(response.json)
