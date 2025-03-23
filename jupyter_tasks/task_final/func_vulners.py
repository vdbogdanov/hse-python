import requests


def vulners_search(api_key, program, version):
    url = "https://vulners.com/api/v3/burp/softwareapi/"
    data = {
        "software": program,
        "version": version,
        "type": "software",
        "apiKey": api_key
    }
    response = requests.post(url, json=data)
    return response.json()
