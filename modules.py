
import requests
import sys

def request_word_from_api(category):
    url = 'https://random-words-api.kushcreates.com/api'
    try:
        request_params = {'language': 'en', 'category': category, 'length': 5, 'type': 'lowercase', 'words': 1}
        response = requests.get(url, headers={"Accept": "application/json"}, params=request_params)
        if response.ok:
            data = response.json()
            word = (data[0]['word'])
            # print(word)
            return word
        else:
            print(f'Encountered an error: HTTP Status Code: {response.status_code}')
            print(f"Please try again later")
            sys.exit(0)
    except requests.exceptions.ConnectionError  as e:
        print(f"Connection failed! The server might be down or your internet is disconnected.")
        print(f"Details: {e}")
        sys.exit(0)
    except requests.exceptions.Timeout as e:
        print("The request timed out.")
        sys.exit(0)
    except requests.exceptions.RequestException as e:
        print(f"A generic requests error occurred: {e}")
        sys.exit(0)