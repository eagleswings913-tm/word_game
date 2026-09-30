import requests

response = requests.get('https://random-words-api.kushcreates.com/api?language=en&category=birds&length=5&type=lowercase&words=5', headers={"Accept": "application/json"})
if response.ok:
    print(response.status_code)
    json_response = response.json()
    # print(json_response)
    for item in json_response:
        print(item['word'])
else:
    print(f'Encountered an error: HTTP Status Code: {response.status_code}')