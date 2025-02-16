import os, base64, json, requests
from dotenv import load_dotenv

load_dotenv()


def virustotal_sendfile(api_key, file_path, file_password):
    url = "https://www.virustotal.com/api/v3/files"
    files = {
        "file": (file_path.split("/")[-1], open(file_path, "rb"), "application/zip")
    }
    headers = {"accept": "application/json", "x-apikey": api_key}

    if file_password:
        payload = {"password": file_password}
        response = requests.post(url, data=payload, files=files, headers=headers)
    else:
        response = requests.post(url, files=files, headers=headers)

    if response.status_code == 200:
        print("\nФайл успешно отправлен на сканирование!")
        print("\nОтвет от сервера:", json.dumps(response.json(), indent=4))
        file_id = response.json()["data"]["id"]
        file_id_decoded = base64.b64decode(file_id).decode("utf-8").split(":")[0]
        return file_id_decoded
    else:
        print("\nОшибка при отправке файла:", response.status_code)
        print("\nТекст ошибки:", response.text)
        return 0


def virustotal_analyzer(api_key, file_id):
    url = f"https://www.virustotal.com/api/v3/files/{file_id}"
    headers = {"accept": "application/json", "x-apikey": api_key}
    response = requests.get(url, headers=headers)
    print("\nСсылка для анализа:", url)
    print("\nОтвет от сервера:", json.dumps(response.json(), indent=4))
    return response.json()


vt_api_key = os.environ.get("VIRUSTOTAL_API_KEY")
vt_file_path = os.environ.get("VIRUSTOTAL_FILE_PATH")
vt_file_password = os.environ.get("VIRUSTOTAL_FILE_PASSWORD")

file_id = virustotal_sendfile(
    api_key=vt_api_key, file_path=vt_file_path, file_password=vt_file_password
)

report = virustotal_analyzer(api_key=vt_api_key, file_id=file_id)
